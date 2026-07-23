from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_pdf(filename="sample_contract.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    
    lines = [
        "SAMPLE VENDOR SERVICE AGREEMENT",
        "",
        "1. Data Handling:",
        "Vendor will process customer data. Data will be stored using standard encryption at rest (AES-128).",
        "",
        "2. Liability:",
        "Vendor limits its total liability for any data breach, confidentiality breach, or negligence to $50,000 USD total.",
        "",
        "3. Termination:",
        "Either party may terminate this agreement with 7 days written notice without cause.",
        "",
        "4. Subcontracting:",
        "Vendor reserves the right to subcontract services to overseas third parties at its sole discretion."
    ]
    
    y = 750
    for line in lines:
        c.drawString(50, y, line)
        y -= 25
        
    c.save()
    print(f"✅ Real PDF created successfully: {filename}")

if __name__ == "__main__":
    create_sample_pdf()