import re
from bs4 import BeautifulSoup as bs
import statistics

def paragraph_detection_fixed_count(text, lines_per_paragraph=20):
    """
    Break the text into paragraphs of exactly `lines_per_paragraph`.
    If the final chunk has fewer lines, it still becomes its own paragraph.
    """
    lines = [l.strip() for l in text.split("\n")]
    paragraphs = []
    current_chunk = []

    for i, line in enumerate(lines):
        current_chunk.append(line)
        # If we reached `lines_per_paragraph` lines, start a new paragraph
        if (i + 1) % lines_per_paragraph == 0:
            paragraphs.append("\n".join(current_chunk))
            current_chunk = []

    # Add any leftover lines as the last paragraph
    if current_chunk:
        paragraphs.append("\n".join(current_chunk))

    return paragraphs

def escape_special_chars(text):
    # Remove or replace special characters that might interfere with XML
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("•", "")
                .replace("~", "")
                .replace("(", "")
                .replace(")", "")
                .replace("■", "")
                .replace("}", ""))

title = "Gertrude"
author = "Hermann Hesse"
year = "1910"
genre = "Novel"
originalrlanguage = "German"
source = "https://www.holybooks.com/wp-content/uploads/Gertrude-By-Hermann-Hesse.pdf"
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

# Adjust the file path as needed
with open(r"Project\plain_text_hesse\gertrude.txt", encoding="utf8") as input_file:
    text = input_file.read()
    text = escape_special_chars(text)

    # Instead of punctuation-based detection, we do fixed 20-line paragraphs
    paragraphs = paragraph_detection_fixed_count(text, lines_per_paragraph=20)

tei_body = "<text>\n"
in_text = False
in_div = False
in_para = False

for para in paragraphs:
    # Check if we reach the place to start <body>:
    # e.g., if "Chapter one" in this paragraph
    if in_text == False and re.search(r"Chapter one", para, re.IGNORECASE):
        in_text = True
        tei_body += "<body>\n"

    if in_text:
        # If we detect a chapter heading like "Chapter x"
        if re.search(r"Chapter [a-z]+", para, re.IGNORECASE):
            # Close the previous <div> if any
            if in_div:
                tei_body += "</div>\n"
            # Open a new <div> with a <head>
            match_chapter = re.search(r"(Chapter [a-z]+)", para, re.IGNORECASE)
            # We'll separate out the heading text from the rest
            if match_chapter:
                heading_text = match_chapter.group(1)
                # Start a new div with head
                tei_body += "<div>\n<head>" + heading_text + "</head>\n"
                # Remove the heading from para text so it doesn’t repeat
                # or you can keep it if you prefer
                rest_text = para.replace(heading_text, "").strip()
                if rest_text:
                    tei_body += "\n<p>\n" + rest_text + "\n</p>\n"
            in_div = True
        else:
            # Regular paragraph content
            # Insert a blank line before and after to highlight the paragraph
            #   as requested
            tei_body += "\n<p>\n" + para + "\n</p>\n"

tei_body += "</body>\n</text>\n"

tei = f'<?xml version="1.0" encoding="UTF-8"?>\n<TEI>\n{tei_header}\n{tei_body}\n</TEI>'
soup = bs(tei, "xml")

with open(r"Project\plain_text_hesse\gertrude.tei", "w", encoding="utf8") as output:
    # Prettify the final XML
    output.write(soup.prettify())