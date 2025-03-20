import re
from bs4 import BeautifulSoup as bs

# set the chapter name to help detection
chapter_names=[
    'THE SON OF THE BRAHMAN',
    'WITH THE SAMANAS',
    'GOTAMA',
    'AWAKENING',
    'KAMALA',
    'WITH THE CHILDLIKE PEOPLE',
    'SANSARA',
    'BY THE RIVER',
    'THE FERRYMAN',
    'THE SON',
    'OM',
    'GOVINDA'
]

title = "Siddhartha"
author = "Hermann Hesse"
year = "1922"
genre = "Novel"
originalrlanguage = "German"
source = "https://www.gutenberg.org/ebooks/2500"
originalfileformat = "Plain text"

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
with open (r"Project\plain_text_hesse\siddhartha.txt", encoding = "utf8") as input:
    in_text = False   # track if actual text start 赋值给in_text
    in_div = False   # track if the chapter start
    in_para = False   # track if the paragraph start
    count = 0   # counter to track chapter 
    
    for line in input:
        line_stripped = line.strip()
        if in_text == False and line_stripped == 'THE SON OF THE BRAHMAN':   # first chapter mean actual text start 保证in_text还保持Flase，证明我们还没有开始actual text
            in_text = True   #改变in_text的值，证明actual text开始
            tei_body += "<body>"   # add text start tag
        if in_text == True and count < len(chapter_names):  #start process since the actual text start
            if line_stripped == chapter_names[count]:   # when find chapter name, means last chapter is end
                if in_div == True:   # if already in div tag, means a new chapter is start
                    tei_body += "</div>\n"   # add chapter end tag
                tei_body += f"<div>\n<head>{chapter_names[count]}</head>\n"  # add tag and put the chapter name inside of head tag
                in_div = True   # mean chapter start 
                count += 1
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
    with open(r"Project\plain_text_hesse\siddhartha.tei", "w", encoding = "utf8") as output:
        output.write(soup.prettify())