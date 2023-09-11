print("Welcome to Python Pizza")
size = input("choose the size of your pizza. S, M, or L? ")
add_peperoni = input("do you want to add peperoni?  Y or N: ")
extra_cheese = input("do you need extra cheese? Y or N: ")
bill = 0
if size == "S":
  bill = 15
  if add_peperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  print(f"Your total bill is {bill}")

elif size == "M":
  bill = 20
  if add_peperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your total bill is {bill}")

elif size == "L":
  bill = 25
  if add_peperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your total bill is {bill}")
