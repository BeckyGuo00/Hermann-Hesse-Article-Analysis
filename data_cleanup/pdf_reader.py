from PyPDF2 import PdfReader
with open (r"C:/Users/becky/DIGS-20031/Project/In_Sight_of_Chaos.txt", "w", encoding= "utf8") as output:
    reader = PdfReader("In_Sight_of_Chaos.pdf")
    for page in reader.pages:
        text = page.extract_text() # + "\n"
        output.write(text)
