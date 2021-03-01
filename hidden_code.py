#This program creates a four-digit pin from randomly-selected numbers; it then gives the user 12 attempts to guess the number. 

from random import randint
number = ""

while len(number) < 4:
    random_digit = str(randint(0, 9))
    number += random_digit

code = list(number)
hidden_code = []
hidden_code.extend(code)
for i in range(len(hidden_code)):
    hidden_code[i] = "*"

guesses = 0
numbers_not_in_code = []

while guesses < 12:
    if hidden_code == code:
        break
        print("You guessed the code: ","".join(code))
    user_guess = list(input("enter a four digit number: "))
    if len(user_guess) > 4:
        print("That's too long")
        user_guess = list(input("enter a four digit number: "))
    guesses += 1
    for i in range(len(user_guess)):
        if user_guess[i] not in code:
            if user_guess[i] not in numbers_not_in_code:
                numbers_not_in_code.append(user_guess[i])
        elif user_guess[i] == code[i]:
            hidden_code[i] = user_guess[i]
        elif (user_guess[i] in code) and (user_guess[i] != code[i]):
            print("Number (",user_guess[i],") in code but wrong position given.")
    for i in range(13):
        if i == 12:
            if guesses == 1:
                print("One guess used. Numbers not in code: ",numbers_not_in_code)
            else:
                print(guesses,"guesses used. Numbers not in code: ",numbers_not_in_code)
            print("Hidden code:","".join(hidden_code),"Numbers not in code: ",numbers_not_in_code)

if guesses == 12:
    print("Out of guesses. Digits guessed correctly:", hidden_code)
elif hidden_code == code:
    code = "".join(code)
    print("Code: ", code, ". Completed in", guesses, "guesses.")
        #elif (user_guess[i] in code) and (user_guess[i] != code[i]):
