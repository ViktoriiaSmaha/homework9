file = open("1_text.txt", "r")
text = file.read()
text_normalized = ""

for i in text:
    if i.isdigit():
        text_normalized = text_normalized + i
    else:
        text_normalized = text_normalized + " "

result = text_normalized.split(" ")
final = []
for i in result:
    if i.isdigit():
        final.append(int(i))
print(final)
