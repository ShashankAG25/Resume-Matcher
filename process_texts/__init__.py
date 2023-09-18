import PyPDF2
import pdfplumber


def clean_text(filePath):
    file = open(filePath, 'rb')
    readFile = PyPDF2.PdfReader(file)
    pages = len(readFile.pages)

    cleanedFile = []
    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()  # Extract the texts from each pages
            cleanedFile.append(text)

    cleanedFile = ''.join(cleanedFile)  # Joining with empty separator
    cleanedReturn = cleanedFile.replace("\n", " ")  # Replace the new lines with white space

    return cleanedReturn


def clean_list(jdRow):
    cleanedFile = ''.join(jdRow)  # Joining with empty separator
    cleanedReturn = cleanedFile.replace("\n", " ")  # Replace the new lines with white space
    return cleanedReturn
