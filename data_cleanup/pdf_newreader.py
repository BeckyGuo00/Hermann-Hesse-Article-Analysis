import fitz

def extract_paragraphs(pdf_path):
    doc = fitz.open(pdf_path)
    paragraphs = []

    for page in doc:
        text = page.get_text("text")  # Extract clean text
        lines = text.split("\n")  # Split into lines

        current_paragraph = []
        for line in lines:
            if line.strip():  # If line is not empty
                current_paragraph.append(line.strip())
            else:
                if current_paragraph:  # Empty line means new paragraph
                    paragraphs.append(" ".join(current_paragraph))
                    current_paragraph = []

        if current_paragraph:  # Add the last paragraph if any
            paragraphs.append(" ".join(current_paragraph))

    # Format paragraphs with new lines before and after
    formatted_text = "\n\n".join(f"\n{para}\n" for para in paragraphs)

    return formatted_text

pdf_path ="C:/Users/becky/DIGS-20031/Project/Beneath the Wheel.pdf"
formatted_text = extract_paragraphs(pdf_path)
with open (r"C:\Users\becky\DIGS-20031\Project\plain_text_hesse\beneath_the_wheel_old.txt" , "w", encoding= "utf8") as output:
    output.write(formatted_text)