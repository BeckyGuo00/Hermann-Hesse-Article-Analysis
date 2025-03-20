import re
from bs4 import BeautifulSoup as bs

# chapter name detector
chapter_names = [
    "Early Spring",
    "My Recollections of Knulp", 
    "The End"
]



title = "Knulp"
author = "Hermann Hesse"
year = "1915"
genre = "Fiction"
originalrlanguage = "German"
source = "https://www.infobooks.org/book/three-tales-from-the-life-of-knulp-hermann-hesse/"
originalfileformat = "PDF"

tei_header = f"""
<teiHeader>
    <fileDesc>
        <titleStmt>
            <title>{title}</title>
            <author>{author}</author>
            <year>{year}</year>
            <genre>{genre}</genre>
            <originalrlanguage>{originalrlanguage}</originalrlanguage>
            <source>{source}</source>
            <originalfileformat>{originalfileformat}</originalfileformat>
        </titleStmt>
    </fileDesc>  
</teiHeader>  
"""


with open (r"Project\plain_text_hesse\knulp.txt", encoding = "utf8") as input:
    tei_body = "<text>"
    in_text = False
    in_div = False
    in_para = False
    count = 0
    

    for line in input:
        line_stripped = line.strip()
        if in_text == False and line_stripped.startswith('Early Spring'):
            in_text = True
            tei_body += "<body>"
        if in_text == True:
            if count < len(chapter_names) and line_stripped.startswith(chapter_names[count]):
                if in_div == True:
                    tei_body += "</div>\n"
                tei_body += f"<div>\n<head>{chapter_names[count]}</head>\n"
                in_div = True
                count += 1
            elif re.search(r"\w", line):
                if in_para == False:
                    tei_body += "<p>\n"
                    in_para = True 
                tei_body += line 
            elif not re.search(r"\w", line):
                if in_para == True:
                    tei_body += "</p>\n"
                    in_para = False
    tei_body += "</body>\n</text>\n"
    tei = f'<?xml version="1.0" encoding="UTF-8"?>\n<TEI>\n{tei_header}\n{tei_body}\n</TEI>'
    soup = bs(tei, "xml")
    with open(r"Project\plain_text_hesse\knulp.tei", "w", encoding = "utf8") as output:
        output.write(soup.prettify())
            
                
                    