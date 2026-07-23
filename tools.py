import os
from pypdf import PdfReader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 1. Initialize local HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Load the persisted vector database
DB_PATH = "./chroma_db"
vector_store = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings,
    collection_name="company_policies"
)

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract full text from a contract PDF file."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
    
    reader = PdfReader(pdf_path)
    extracted_text = ""
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            extracted_text += f"\n--- Page {page_num + 1} ---\n" + text
            
    return extracted_text

def query_relevant_policies(contract_clause: str, top_k: int = 3) -> list:
    """Query ChromaDB for company policies relevant to a contract clause."""
    results = vector_store.similarity_search_with_score(contract_clause, k=top_k)
    matched_policies = []
    
    for doc, score in results:
        matched_policies.append({
            "policy_id": doc.metadata.get("id"),
            "category": doc.metadata.get("category"),
            "content": doc.page_content,
            "relevance_score": float(score)
        })
        
    return matched_policies