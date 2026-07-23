import gradio as gr
import json
from agent import audit_contract_pdf

def process_contract_file(file_obj):
    """Callback function for Gradio interface."""
    if file_obj is None:
        return "⚠️ Please upload a valid PDF contract file.", ""

    file_path = file_obj.name
    
    try:
        # Run audit
        result = audit_contract_pdf(file_path)
        
        # Extract execution info
        latency = result.get("execution_latency_seconds", 0)
        cost = result.get("estimated_cost_usd", 0.0)
        
        metrics_summary = f"⏱️ Execution Time: {latency}s | 💰 Cost: ${cost} USD | ⚡ Model: Groq LLaMA 3.3 70B"
        
        # Return formatted JSON
        audit_report = result.get("audit_report", {})
        formatted_json = json.dumps(audit_report, indent=2)
        
        return metrics_summary, formatted_json

    except Exception as e:
        return f"❌ Error processing file: {str(e)}", ""

# Define Gradio UI Layout
with gr.Blocks(title="Automated Contract Audit & Compliance Pipeline") as demo:
    gr.Markdown(
        """
        # 📜 Automated Contract Audit & Vendor Compliance Pipeline
        ### Powered by Groq (LLaMA 3.3 70B) & ChromaDB (Vector Search)
        Upload a vendor contract PDF to perform an automated security & legal compliance evaluation.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="Upload Contract (PDF)", file_types=[".pdf"])
            submit_btn = gr.Button("🔍 Run Audit Engine", variant="primary")
            
        with gr.Column(scale=2):
            status_output = gr.Textbox(label="Execution Metrics", interactive=False)
            json_output = gr.Code(label="Audit Findings (JSON Report)", language="json")

    submit_btn.click(
        fn=process_contract_file,
        inputs=[file_input],
        outputs=[status_output, json_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)