#seperate pdf into pic
import os
from pdf2image import convert_from_path

#use tiff format for best OCR, but takes more disk space. Use png if space contrained: OCR output may be worse.
# ON WINDOWS, make sure define the poppler_path keyword to tell pdf2image where to find poppler:
images = convert_from_path("Peter Camenzind.pdf", fmt = "tiff", dpi = 400, poppler_path = r"C:/Program Files/poppler-23.01.0/Library/bin")

os.mkdir("images")
page_count = 1
for image in images:
    page_image_name = f"images/page-{page_count}.tiff"
    image.save(page_image_name, format = "tiff") # image object has a save method with 2 args: path & format
    page_count += 1 

#from pic to text
import pytesseract
from bs4 import BeautifulSoup as bs

#set the path to the tesseract binary 
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe" 
page_images = range (3, 210)    # the last page will not be include

with open ("peter_camenzind.txt", "w", encoding = "utf8") as output:
    for page in page_images:
        page_path = f"images/page-{page}.tiff"
        print(f"Processing{page_path}...")   #keep track of progress
        xml = pytesseract.image_to_alto_xml(page_path)
        soup = bs(xml, "xml")
        text_blocks = soup.find_all("TextBlock")   #a TextBlock is typically a paragraoh
        for text_block in text_blocks:
            text_lines = text_block.find_all("TextLine")   #find each line within block
            paragraph = []
            for text_line in text_lines:
                strings_tags = text_line.find_all("String")   #find each word
                line = []
                for string_tag in strings_tags:
                    line.append(string_tag["CONTENT"])
                line_for_text = " ".join(line)   #inser spaces between words
                paragraph.append(line_for_text)
            paragraph_text = "\n".join(paragraph)   #inser newlines between lines
            output.write(f"{paragraph_text}\n\n")   #blank line between paragraphs
        output.write("\n\n")   #add a blank line between pages