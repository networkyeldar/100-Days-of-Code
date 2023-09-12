import random

names_string = input("Give me everybody's name separated by comma.")
names = names_string.split(",")
c = random.randint(1,len(names))
print(f"{names[c]} will pay!")
