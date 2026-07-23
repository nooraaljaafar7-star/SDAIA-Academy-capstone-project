import json
from agent import audit_contract_pdf

# Run full evaluation on our sample contract PDF file
print("⏳ Executing LLM Contract Audit with Groq...\n")

result = audit_contract_pdf("sample_contract.pdf")

print("="*60)
print(f"⏱️ Execution Latency: {result['execution_latency_seconds']} seconds")
print(f"💰 Estimated Cost: ${result['estimated_cost_usd']} USD")
print("="*60)
print("\n📊 AUDIT REPORT OUTPUT:\n")
print(result["raw_response"])