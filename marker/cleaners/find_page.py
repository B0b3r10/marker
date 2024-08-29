import pdfplumber

def find_pages_with_text(pdf_path, search_text):
    pages_with_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if search_text in text:
                pages_with_text.append(i + 1)
    return pages_with_text