import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    try:
        content = file.file.read()
        pdf = fitz.open(stream=content, filetype="pdf")
        text = ""

        for page in pdf:
            text += page.get_text()

        return text.strip()

    except Exception as e:
        raise Exception(f"PDF parsing error: {str(e)}")