import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number"))
    if user == number:
        print('Hurray!!')
        print(f"Great number guessing power and its  {number}")
        break
if user!=number:
    print(f"Guess is incorrect the number is {number}")