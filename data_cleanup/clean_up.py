import re    


# clean up the websit 
"""with open(r"C:/Users/becky/DIGS-20031/Project/beneath_the_wheel.txt", encoding = "utf8") as input:
    file = input.readlines()

pattern = re.compile("Downloaded from https://www.holybooks.com")

with open(r"C:/Users/becky/DIGS-20031/Project/beneath_the_wheel_new.txt", "w", encoding= "utf8") as output:
    for line in file:
        newline = pattern.sub("", line)
        output.write(newline)"""
        


# clean up extra chapter name        
"""with open(r"Project\plain_text_hesse\peter_camenzind.txt", "r", encoding = 'utf-8') as input:
    file = input.readlines()


with open(r"Project\plain_text_hesse\peter_camenzind_new.txt", "w", encoding = 'utf-8') as output:
    for line in file:
        if re.match(r"^CHAPTER\s+[A-Z]+\b", line):
            continue
        output.write(line)"""


"""# clean up extra words
with open(r"Project\Beneath-the-Wheel.txt", "r", encoding = 'utf-8') as input:
    file = input.readlines()

pattern = re.compile("           Downloaded from https://www.holybooks.com")
with open(r"Project\plain_text_hesse\Beneath-the-Wheel.txt", "w", encoding = 'utf-8') as output:
    for line in file:
        newline = pattern.sub('', line)
        output.write(newline)"""
        
        
    
with open ("C:/Users/becky/DIGS-20031/Project/Steppenwolf.txt", encoding='utf8') as input:
    content = input.read()

# Split the text into paragraphs.
# This example assumes that a paragraph ends with a punctuation mark (.!?)
# followed by one or more spaces and then a capital letter.
paragraphs = re.split(r'(?<=[.!?])\s+(?=[A-Z])', content)

# Join paragraphs with two newline characters (one blank line between paragraphs)
formatted_text = '\n\n'.join(para.strip() for para in paragraphs)

# Write the reformatted text to a new file
with open("C:/Users/becky/DIGS-20031/Project/steppenwolf.txt", 'w', encoding='utf-8') as file:
    file.write(formatted_text)
