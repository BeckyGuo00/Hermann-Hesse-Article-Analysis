import re

def clean_line(line):
    # Remove unwanted phrases (case-insensitive) and extra spaces.
    line = re.sub(r'\b(HERMANN HESSE|IN SIGHT OF CHAOS)\b', '', line)
    # Collapse multiple spaces into one and strip leading/trailing whitespace.
    return re.sub(r'\s+', ' ', line).strip()

# Read all lines from the file.
with open("In_Sight_of_Chaos.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Remove form feed characters.
text = text.replace("\f", " ")

# Remove lines that are only page numbers.
# Split the text into lines, filter out those that match a page number pattern,
# then join them back with newlines.
lines = text.splitlines()
lines = [line for line in lines if not re.match(r'^\s*\d+\s*$', line)]
text = "\n".join(lines)

# Remove unwanted phrases.
# Use regex patterns that allow for one or more whitespace characters between words.
text = re.sub(r'\bHERMANN\s+HESSE\b', '', text, flags=re.IGNORECASE)
text = re.sub(r'\bIN\s+SIGHT\s+OF\s+CHAOS\b', '', text, flags=re.IGNORECASE)

# Assume that paragraphs are meant to be separated by at least one blank line.
# Replace two or more newline characters with a special marker.
text = re.sub(r'\n{2,}', '<<<PARA>>>', text)

# Replace any remaining single newline characters (hard wraps) with a space.
text = re.sub(r'\n', ' ', text)

# Collapse multiple spaces into one.
text = re.sub(r'\s+', ' ', text)

# Now split the text at the paragraph marker and trim each paragraph.
paragraphs = [para.strip() for para in text.split("<<<PARA>>>") if para.strip()]

# Join paragraphs with two newlines before and after each paragraph.
cleaned_text = "\n\n".join(paragraphs)
cleaned_text = "\n" + cleaned_text + "\n"

# Write the cleaned text to a new file.
with open("In_Sight_of_Chaos_cleaned.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)