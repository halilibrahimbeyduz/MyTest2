from pdf2docx import Converter

pdf_path = "umre.pdf"
docx_path = "umre.docx"

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()

print("test")