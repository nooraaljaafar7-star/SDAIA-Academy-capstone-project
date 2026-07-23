import os
import json
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from tools import extract_text_from_pdf, query_relevant_policies

# Load environment variables
load_dotenv()

# Initialize Groq LLM (Free & Fast)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# System Prompt for Legal Audit
SYSTEM_PROMPT = """
You are an expert AI Legal & Compliance Auditor. Your task is to analyze contract text against company compliance policies.

For each potential issue or clause in the contract:
1. Compare it with the retrieved company policies.
2. Identify compliance status: [COMPLIANT], [NON-COMPLIANT], or [NEEDS REVIEW].
3. Highlight any risks and provide a recommended amendment.

Output your analysis strictly in valid JSON format with the following keys:
- "audit_summary": string
- "overall_status": string ("APPROVED", "REJECTED", "NEEDS_REVISION")
- "findings": list of objects containing ("clause", "matched_policy_id", "status", "risk_level", "explanation", "recommendation")
"""

def audit_contract_pdf(pdf_path: str) -> dict:
    """Main function to parse, evaluate, and produce an immutable compliance audit report."""
    start_time = time.time()
    
    # Step 1: Extract Text
    contract_text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Retrieve Relevant Policies for the Contract
    retrieved_policies = query_relevant_policies(contract_text, top_k=5)
    
    # Prepare Prompt Inputs
    policies_context = "\n".join([f"[{p['policy_id']}] {p['content']}" for p in retrieved_policies])
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "COMPANY POLICIES:\n{policies}\n\nCONTRACT TEXT:\n{contract}")
    ])
    
    # Step 3: Run LLM Audit
    chain = prompt | llm
    response = chain.invoke({
        "policies": policies_context,
        "contract": contract_text
    })
    
    latency = round(time.time() - start_time, 2)
    
    # Parse LLM response content string to structured JSON dict
    raw_content = response.content.strip()
    if raw_content.startswith("```json"):
        raw_content = raw_content.replace("```json", "").replace("```", "").strip()
        
    try:
        parsed_audit = json.loads(raw_content)
    except Exception:
        parsed_audit = {"raw_output": response.content}

    return {
        "execution_latency_seconds": latency,
        "estimated_cost_usd": 0.0,
        "audit_report": parsed_audit
    }