import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from agent import audit_contract_pdf
from tracing import setup_tracing
setup_tracing()

app = FastAPI(
    title="Automated Contract Audit & Vendor Compliance Pipeline",
    description="An AI-powered security & legal compliance tool using Groq, ChromaDB, and FastAPI.",
    version="1.0.0"
)

# Folder to store uploaded PDF contracts temporarily
UPLOAD_DIR = "./uploaded_contracts"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "Automated Contract Audit API",
        "llm_engine": "Groq LLaMA 3.3 70B",
        "cost": "Free Tier"
    }

@app.post("/audit-contract/")
async def audit_contract_endpoint(file: UploadFile = File(...)):
    """Upload a PDF contract to evaluate compliance against corporate policies."""
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save the uploaded file locally
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Run the audit process
        audit_result = audit_contract_pdf(file_path)
        
        return JSONResponse(status_code=200, content={
            "filename": file.filename,
            "status": "success",
            "audit_data": audit_result
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up the file after processing
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)