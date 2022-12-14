file = open("5_text.txt")
text = file.read()
text_normalized = ""

for i in text:
    if i.isdigit() or i.isspace():
        text_normalized = text_normalized + " "
    else:
        text_normalized = text_normalized + i

result = text_normalized.split(" ")

final = []
for i in result:
    if i.isalpha():
        final.append(i)

count = len(final)

print(count)
