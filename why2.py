import random
randomnumber = random.randint(0,10)
guess = 0
attempt = 0
while guess != randomnumber:
    attempt += 1
    guess = float(input('guess a number between 0 to 10: '))
    if guess < randomnumber:
        print(f"{guess} is to low")
    elif guess > randomnumber:
        print(f"{guess} is too high")
print(f"Congratulations you found the number in {attempt} attempts ! ")