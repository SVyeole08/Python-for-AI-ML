import random
com =  random.randint(1,100)
tries = 0

while True:
    hum = int(input("Guess the number between 1 - 100 :-"))
    tries+=1
    if com == hum:
        print(f"Congratulations! You guessed the number in {tries} tries!")
        break
    elif com > hum:
        print("Sorry! Go higher.")
    elif com < hum:
        print("Sorry! Go lower.")
    else:print("Try to guess between 1 - 100")

