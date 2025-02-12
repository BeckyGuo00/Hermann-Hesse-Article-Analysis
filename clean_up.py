import re



with open(r"C:/Users/becky/DIGS-20031/Project/beneath_the_wheel.txt", encoding = "utf8") as input:
    file = input.readlines()

pattern = re.compile("Downloaded from https://www.holybooks.com")

with open(r"C:/Users/becky/DIGS-20031/Project/beneath_the_wheel_new.txt", "w", encoding= "utf8") as output:
    for line in file:
        newline = pattern.sub("", line)
        output.write(newline)