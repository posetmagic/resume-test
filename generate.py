from weasyprint import HTML
from PyPDF2 import PdfReader, PdfWriter
import io
import os

def convert_to_exact_a4(html_file, output_pdf):
    # A4 dimensions in points (1 point = 1/72 inch)
    # A4 is 210mm × 297mm = 595.276 × 841.890 points
    A4_WIDTH = 595.276
    A4_HEIGHT = 841.890

    # First create PDF in memory
    pdf_buffer = io.BytesIO()
    HTML(filename=html_file).write_pdf(pdf_buffer, options={'page-size': 'A4'})
    pdf_buffer.seek(0)

    # Create PDF reader and writer
    reader = PdfReader(pdf_buffer)
    writer = PdfWriter()

    # Process each page
    for page in reader.pages:
        # Scale page to fit A4
        page.scale_to(A4_WIDTH, A4_HEIGHT)
        # Set MediaBox to A4 dimensions
        page.mediabox.upper_right = (A4_WIDTH, A4_HEIGHT)
        page.mediabox.lower_left = (0, 0)
        # Add the modified page to the writer
        writer.add_page(page)

    # Write the final PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# Directory to search for HTML files
directory = "./"  # Change this to the folder you want to search in

# Loop through all directories and files
for root, dirs, files in os.walk(directory):
    for file in files:
        if file == "resume.html":
            html_file = os.path.join(root, file)
            output_pdf = os.path.join(root, "resume.pdf")

            try:
                convert_to_exact_a4(html_file, output_pdf)
                print(f"PDF created successfully with exact A4 dimensions: {output_pdf}")
            except Exception as e:
                print(f"Error creating PDF from '{html_file}': {e}")