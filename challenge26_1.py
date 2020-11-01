from random import randint

number = ""

while len(number) < 4:
    random_digit = str(randint(0, 9))
    number += random_digit#.append(random_digit)

code = list(number)
hidden_code = []
hidden_code.extend(code)
for i in range(len(hidden_code)):
    hidden_code[i] = "*"

print(hidden_code)

guesses = 0
numbers_not_in_code = []
correct_number_guesses = []
correct_position_guesses = 0
correct_guesses = 0

#tells how many digits guessed correctly; how many digits guessed correctly
#in right place, and how many in wrong place

while guesses < 12:
    user_guess = list(input("enter a four digit number: "))
    if len(user_guess) < 4:
        user_guess = list(input("enter a four digit number: "))
    guesses += 1
    for i in range(len(user_guess)):
        if user_guess[i] == code[i]:
            correct_position_guesses += 1
            hidden_code[i] = user_guess[i]
            print("One digit correct. Guess again")
            print(hidden_code)
        elif (user_guess[i] in code) and (user_guess[i] != code[i]):
            print("Correct digit, wrong position")
            correct_guesses += 1
    if hidden_code == code:
        break
        code = "".join(code)
        print("Code: ", code, ". Completed in", guesses, "guesses.")


print("Number of digits guessed correctly:", correct_position_guesses, "Number of correct digits in incorrect places: ", correct_guesses)
