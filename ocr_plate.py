import easyocr
def plate_ocr(plate,languages=['en','ar']):
    reader = easyocr.Reader(languages) # this needs to run only once to load the model into memory
    result = reader.readtext(plate, detail = 0)
    return result
