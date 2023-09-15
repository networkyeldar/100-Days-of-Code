for n in range(1,101):
  if n % 3 == 0 and n % 5 == 0: 
    n = "FizzBuzz"
    fizzbuzz_num += 1
  elif n % 3 == 0:
    n = "Fizz"
  elif n % 5 ==0:
    n = "Buzz"
  print(n)
