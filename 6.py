file = open("sumtext.txt", "r")
lines = file.read()
numbers = lines.split(" ")
summ = 0
print(numbers)
for number in numbers:
    summ = summ + int(number)
print(summ)
