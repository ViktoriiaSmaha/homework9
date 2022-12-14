n = int(input("Enter number"))
file = open("numbers.txt", "w")

for i in range(n):
    number = int(input("Enter your numbers"))
    file.write(str(number) + " ")
