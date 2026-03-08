import fitz  # PyMuPDF


def extract_text_by_page(file_path: str):
    pages = []

    doc = fitz.open(file_path)

    for page_num, page in enumerate(doc):

        text = page.get_text()

        pages.append({
            "page": page_num + 1,
            "text": text
        })

    doc.close()

    return pages