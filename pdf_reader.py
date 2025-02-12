from PyPDF2 import PdfReader
with open (r"C:/Users/becky/DIGS-20031/Project/Steppenwolf.txt", "w", encoding= "utf8") as output:
    reader = PdfReader("Steppenwolf.pdf")
    for page in reader.pages:
        text = page.extract_text() # + "\n"
        output.write(text)
        
