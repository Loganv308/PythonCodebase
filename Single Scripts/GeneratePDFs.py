from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(pdf_file_name):
    # Create a new PDF with reportlab
    c = canvas.Canvas(pdf_file_name, pagesize=letter)
    c.drawString(100, 750, "Hello, World!")
    c.showPage()
    c.save()

# Example usage
generate_pdf("hello_world.pdf")
