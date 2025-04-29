from pypdf import PdfReader
import json

def readPDF(path:str)->str:
   # importing required classes


    # creating a pdf reader object
    reader = PdfReader(path)

    # printing number of pages in pdf file
    print(len(reader.pages))
    pdf_text = ""
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        pdf_text = pdf_text + page.extract_text()
        print(page.extract_text())
    
    return pdf_text


def convert_to_json(text:str)->json:
    try:
        json_data = json.loads(text)
        print(json_data)
        print(type(json_data))
        return json_data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")