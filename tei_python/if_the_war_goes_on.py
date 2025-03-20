import re
from bs4 import BeautifulSoup as bs

title = "If The War Goes On"
author = "Hermann Hesse"
year = "1946"
genre = "Fiction"
originalrlanguage = "German"
source = "https://ratical.org/ratville/JFK/IfTheWarGoesOn.pdf"
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
with open (r"Project\plain_text_hesse\if_the_war_goes_on.txt", encoding = "utf8") as input:
    in_text = False
    in_div = False
    in_para = False
    for line in input:
        if in_text is False and "Chapter one" in line:
            in_text = True
            tei_body += "<body>"
        if in_text is True:
            if re.search(r"Chapter [a-z]+", line):
                if in_div is True:
                    tei_body += "</div>\n"
                line = re.sub(r"(Chapter [a-z]+)", r"<div>\n<head>\1</head>", line)
                in_div = True
                tei_body += line
            elif re.search(r"\w", line):
                if in_para is False:
                    tei_body += "<p>\n"
                    in_para = True
                tei_body += line
            elif not re.search(r"\w", line):
                if in_para is True:
                    tei_body += "</p>\n"
                    in_para = False
    tei_body += "</body>\n</text>\n"   #we close the last div, and the body tag
    tei = f'<?xml version="1.0" encoding="UTF-8"?>\n<TEI>\n{tei_header}\n{tei_body}\n</TEI>'
    soup = bs(tei, "xml")
    with open(r"Project\plain_text_hesse\if_the_war_goes_on.tei", "w", encoding = "utf8") as output:
        output.write(soup.prettify())