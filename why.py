guess = 0
while guess!=5:
    guess=int(input("Gissa på ett tal: "))

if guess <5:
    print(f"Din gissning {guess} är för liten")
elif guess >5:
        print(f"Din gissning {guess} är för stor")

print("Grattis du gissade rätt! ")        