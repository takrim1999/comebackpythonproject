from random import randint
import os

if not os.path.exists("log.txt"):
    with open("log.txt", "w") as log:
        log.write(log.write("number attempt\n"))

number = randint(1, 1000)

attempt = 0

while True:
    attempt += 1
    num = int(input("guess: "))
    if num == number:
        print("you found it!")
        break
    elif num > number:
        print("you've choosen bigger!")
    elif num < number:
        print("you've choosen smaller!")
    else:
        print("not correct! Try again!")
    if attempt == 9:
        print("last attempt")
    if attempt >= 10:
        print("Game Over!")
        break
with open("log.txt", "a") as log:
    log.write(f"{number} {attempt}\n")
