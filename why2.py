import random
randomnumber = random.randint(0,10)
guess = 0
attempt = 1
while guess != randomnumber:
    guess = float(input('guess a number between 0 to 10: '))
    if guess < randomnumber:
        print(f"{guess} is to low")
        attempt += 1
    elif guess > randomnumber:
        print(f"{guess} is too high")
        attempt += 1
    else:
        print(f"Congratulations you found the number in {attempt} attempts ! ")