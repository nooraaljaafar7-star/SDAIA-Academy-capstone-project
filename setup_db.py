import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 1. تحديد السياسات التنظيمية والقانونية للشركة (Corporate Compliance Policies)
CORPORATE_POLICIES = [
    {
        "id": "POL-001",
        "category": "Data Security & Privacy",
        "content": "All vendor processing operations involving customer data must comply with GDPR and Saudi NDMO data privacy standards. Data must be encrypted at rest (AES-256) and in transit (TLS 1.3)."
    },
    {
        "id": "POL-002",
        "category": "Liability & Compensation",
        "content": "Limitation of liability clauses must not cap vendor liability for data breaches, confidentiality violations, or gross negligence below $1,000,000 USD."
    },
    {
        "id": "POL-003",
        "category": "Termination & Notice",
        "content": "Contracts must include a minimum 30-day notice period for termination without cause. Immediate termination is required upon any security or compliance breach."
    },
    {
        "id": "POL-004",
        "category": "Subcontracting & Third Parties",
        "content": "Vendors are strictly prohibited from subcontracting any part of the service or transferring corporate data to third parties without prior written consent from the security operations team."
    },
    {
        "id": "POL-005",
        "category": "Jurisdiction & Governing Law",
        "content": "All contract disputes and legal claims must be governed exclusively by the laws of Saudi Arabia and settled under local jurisdiction."
    }
]

def init_vector_db():
    print("⏳ Initializing Local Embeddings Model (HuggingFace)...")
    # استخدام موديل مجاني ومحلي بالكامل لتحويل النصوص لمتجهات
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    documents = []
    for policy in CORPORATE_POLICIES:
        doc = Document(
            page_content=policy["content"],
            metadata={"id": policy["id"], "category": policy["category"]}
        )
        documents.append(doc)

    print("💾 Storing policies into ChromaDB local directory...")
    db_path = "./chroma_db"
    
    # حفظ البيانات في مجلد محلي chroma_db
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=db_path,
        collection_name="company_policies"
    )
    
    print("✅ ChromaDB initialized successfully with corporate policies!")

if __name__ == "__main__":
    init_vector_db()