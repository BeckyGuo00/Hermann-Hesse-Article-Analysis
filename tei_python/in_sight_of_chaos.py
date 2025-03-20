import re
from bs4 import BeautifulSoup as bs
import statistics

# find paragraph
def paragraph_detection(text, short_threshold=0.5, long_threshold=1.5):
    lines = [str(line) for line in text]

    # Identify potential paragraph breaks based on sentence endings
    potential_breaks = [i for i, line in enumerate(lines) if line.endswith((".", "!", "?"))]


    # Calculate the median line length
    try:
        median_length = statistics.median(len(line) for line in lines)
    except statistics.StatisticsError:  # no lines of text
        return lines

    # Calculate the mean and standard deviation of line lengths, excluding very short and very long lines
    line_lengths = [
        len(line)
        for i, line in enumerate(lines)
        if i not in potential_breaks and median_length * short_threshold <= len(line) <= median_length * long_threshold
    ]

    if line_lengths and len(line_lengths) > 1:
        mean_length = statistics.mean(line_lengths)
        stdev_length = statistics.stdev(line_lengths)
    else:
        mean_length = median_length
        stdev_length = 0

    paragraphs = []
    current_paragraph = []

    for i, line in enumerate(lines):
        current_paragraph.append(line)

        if i in potential_breaks:
            # Check if the line length deviates significantly from the mean
            if len(line) < mean_length - stdev_length:
                paragraphs.append(" ".join(current_paragraph) + "\n")
                current_paragraph = []

    # Add the last paragraph if it's not empty
    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    return paragraphs

title = "In Sight of Chaos"
author = "Hermann Hesse"
year = "1920"
genre = "Fiction"
originalrlanguage = "German"
source = "https://babel.hathitrust.org/cgi/pt?id=ucbk.ark:/28722/h21j97t9c&seq=1"
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
with open (r"Project/plain_text_hesse/in_sight_of_chaos.txt", encoding = "utf8") as input:
    text = input.read()
    paragraphs = paragraph_detection(text)
    


tei_body = "<text>"
with open (r"Project/plain_text_hesse/in_sight_of_chaos.txt", encoding = "utf8") as input:
    in_text = False
    in_div = False
    in_para = False
    for line in input:
        if in_text is False and "IT APPEARS TO ME THAT WHAT" in line:
            in_text = True
            tei_body += "<body>"
        if in_text is True:
            if re.search(r"\w", line):
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
    with open(r"Project\plain_text_hesse\in_sight_of_chaos.tei", "w", encoding = "utf8") as output:
        output.write(soup.prettify())