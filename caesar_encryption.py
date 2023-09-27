alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(plain_text, shift_amount,direct):
  message = ""
  if direct == "encode":
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
          new_position = new_position - 26
        message += alphabet[new_position]
    print(message)
      
  if direct == "decode":
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position > 25:
          new_position = new_position - 26
        message += alphabet[new_position]
    print(message)
is_the_end = False
while not is_the_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text=text,shift_amount=shift,direct=direction)
  should_continue = input("Type 'yes' ton continue or type 'no' to exit").lower()
  if should_continue == "yes":
      caesar(plain_text=text,shift_amount=shift,direct=direction)
  else:
    is_the_end = True
