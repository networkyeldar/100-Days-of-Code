import random
numbers = []
for number in range(1,101):
  numbers.append(number)

print("Welcome to the Number Guessing Game!!!\nI'm thinking of a number between 1 and 100")
difficulty = input("choose difficulty type 'easy' or 'hard:'")
EASY_LEVEL = 10
HARD_LEVEL = 5
if difficulty == 'easy':
  life = EASY_LEVEL
elif difficulty == 'hard':
  life = HARD_LEVEL
random_number = random.choice(numbers)
print(random_number)
end_of_life = False
while not end_of_life:
  guess = int(input("Make a guess:"))
  if guess!=random_number:
    life -= 1
    if guess > random_number:
      print("Too high. Guess again")
      print(f"You have {life} attemtps")
    elif guess < random_number:
      print("Too low. Guess again")
      print(f"You have {life} attemtps")
  else:
    print("You got it!")
    end_of_life = True
  if life == 0:
    print("You lose!")
    end_of_life = True
