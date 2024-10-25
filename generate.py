from weasyprint import HTML
import os

# Path to your HTML file
html_file = "resume.html"
# Output PDF file name
output_pdf = "resume.pdf"

# Check if the HTML file exists
if not os.path.exists(html_file):
    print(f"Error: The file '{html_file}' does not exist.")
else:
    try:
        # Convert HTML to PDF
        HTML(filename=html_file).write_pdf(output_pdf)
        print(f"PDF created successfully: {output_pdf}")
    except Exception as e:
        print(f"Error creating PDF with WeasyPrint: {e}")
