from img2table.document import Image
from img2table.document import PDF
from IPython.display import display_html
from img2table.ocr import TesseractOCR
import img2pdf
from PIL import Image
import os
from img2table.ocr import EasyOCR

easyocr = EasyOCR(lang=["en"])

img_path = "tt.jpg"
pdf_path = "ff.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
print("Successfully made pdf file")

tesseract_ocr = TesseractOCR(n_threads=1, lang="eng")
# Instantiation of the image
pdf = PDF(src="ff.pdf")

# Extract tables
pdf.to_xlsx('tables.xlsx',
            ocr=easyocr,
            implicit_rows=False,
            borderless_tables=False,
            min_confidence=50)
