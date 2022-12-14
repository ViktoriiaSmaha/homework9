import random
file = open("random_numbers.txt", "w")


for i in range(100):
    number = random.randint(1, 100)
    file.write(str(number) + "\n")

