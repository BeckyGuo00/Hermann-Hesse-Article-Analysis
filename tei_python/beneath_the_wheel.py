import re
from bs4 import BeautifulSoup as bs


# clear up the text , remove special characters
def escape_special_chars(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("•", "").replace("~", "").replace("(", "").replace(")", "").replace("■", "").replace("}", "")
title = "Beneath The Wheel"
author = "Hermann Hesse"
year = "1906"
genre = "Fiction"
originalrlanguage = "German"
source = "https://www.holybooks.com/wp-content/uploads/The-Prodigy-By-Hermann-Hesse.pdf"
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
with open (r"Project/plain_text_hesse/beneath_the_wheel.txt", encoding = "utf8") as input:  
    text = input.read()
    text = escape_special_chars(text) 
    in_text = False   # track if actual text start 赋值给in_text
    in_div = False   # track if the chapter start
    in_para = False   # track if the paragraph start
    for line in text.splitlines():
        if in_text == False and "CHAPTER ONE" in line:   # first chapter mean actual text start 保证in_text还保持Flase，证明我们还没有开始actual text
            in_text = True   #改变in_text的值，证明actual text开始
            tei_body += "<body>"   # add text start tag
        if in_text == True:   # start process since the actual text start
            if re.search(r"CHAPTER [A-Z]+", line):   # when find this reg, means last chapter is end 
                if in_div == True:   # if already in div tag, means a new chapter is start
                    tei_body += "</div>\n"   # add chapter end tag
                line = re.sub(r"(CHAPTER [A-Z]+)", r"<div>\n<head>\1</head>", line)   # add chapter name as head tag context, also add chapter tag before head tag  
                in_div = True   # mean chapter start 
                tei_body += line 
            elif re.search(r"\w", line):   # find any words in line
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
    with open(r"Project/plain_text_hesse/beneath_the_wheel.tei", "w", encoding = "utf8") as output:
        output.write(soup.prettify())