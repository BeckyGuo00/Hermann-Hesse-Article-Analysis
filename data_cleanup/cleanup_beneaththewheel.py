import re
# C:/Users/becky/DIGS-20031/Project/Steppenwolf.txt
# C:/Users/becky/DIGS-20031/Project/steppenwolf.txt

# Read file lines
with open("Beneath-the-Wheel.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Prepare a list to hold cleaned lines
cleaned_lines = []
for line in lines:
    # Skip lines that consist solely of a page number (e.g., "7", "10", etc.)
    if re.match(r'^\s*\d+\s*$', line):
        continue
    # Remove the unwanted string (with any surrounding whitespace)
    line = re.sub(r'\s*Downloaded from https://www\.holybooks\.com\s*', '', line)
    # Remove form feed characters
    line = line.replace("\f", " ")
    # Append the line without its trailing newline
    cleaned_lines.append(line.rstrip('\n'))

paragraphs = []
current_paragraph = []
prev_indent = None

# Process each cleaned line to detect paragraph boundaries by indent change
for line in cleaned_lines:
    stripped_line = line.strip()
    # If the line is empty after stripping, treat it as a forced paragraph break.
    if not stripped_line:
        if current_paragraph:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []
        prev_indent = None
        continue

    # Determine current line's indent (number of leading spaces)
    current_indent = len(line) - len(line.lstrip(' '))

    if current_paragraph:
        # If previous indent exists and the current indent is at least 4 spaces greater,
        # assume this is the start of a new paragraph.
        if prev_indent is not None and (current_indent - prev_indent >= 4):
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = [stripped_line]
        else:
            # Otherwise, assume the line continues the current paragraph.
            current_paragraph.append(stripped_line)
    else:
        current_paragraph.append(stripped_line)

    prev_indent = current_indent

# Append any remaining lines as the last paragraph.
if current_paragraph:
    paragraphs.append(" ".join(current_paragraph))

# Join paragraphs with an empty line (newline before and after each paragraph)
transformed_text = "\n\n".join(paragraphs)

# Optionally, write the output to a new file
with open("Beneath-the-Wheel_transformed.txt", "w", encoding="utf-8") as f:
    f.write(transformed_text)