import re
from bs4 import BeautifulSoup as bs

title = "Steppenwolf"
author = "Hermann Hesse"
year = "1927"
genre = "Novel"
originalrlanguage = "German"
source = "https://www.kkoworld.com/kitablar/Herman_Hesse_Yalquzaq_eng.pdf"
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
tei_body = "<text>"
with open (r"Project/plain_text_hesse/steppenwolf.txt", encoding = "utf8") as input:
    in_text = False   # track if actual text start 赋值给in_text
    in_div = False   # track if the chapter start
    in_para = False   # track if the paragraph start
    for line in input:
        if in_text == False and "FOR MADMEN ONLY" in line:   # first chapter mean actual text start 保证in_text还保持Flase，证明我们还没有开始actual text
            in_text = True   #改变in_text的值，证明actual text开始
            tei_body += "<body>"   # add text start tag
        if in_text == True:   # start process since the actual text start
            if re.search(r"\w", line):   # find any words in line
                if in_para == False:   # means find a new paragraph start
                    tei_body += "<p>\n"   # add para start tag
                    in_para = True   # means para start 
                tei_body += line 
            elif not re.search(r"\w", line):   # fing any non-word line
                if in_para == True:   # mean we still in last para text
                    tei_body += "</p>\n"   # to stop last para
                    in_para = False
    tei_body += "</body>\n</text>\n"   #we close the last div, and the body tag
    tei = f'<?xml version="1.0" encoding="UTF-8"?>\n<TEI>\n{tei_header}\n{tei_body}\n</TEI>'
    soup = bs(tei, "xml")
    with open(r"Project/plain_text_hesse/steppenwolf.tei", "w", encoding = "utf8") as output:
        output.write(soup.prettify())