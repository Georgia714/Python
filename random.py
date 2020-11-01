#SLIDE 21
name = input("What is your name: ")
city = input("Enter the town or city you are from: ")
print("Hello {}. You are from {}.".format(name.capitalize(), city.capitalize()))


#SLIDE 26
import random

myName = input("Hello, what's your name: ")
number = random.randint(1, 10)
print("Well,", myName.capitalize(), ", I am thinking of a number between 1 and 10.")
guess = int(input("Take a guess."))
if guess == number:
    print("Good job, " + myName + "! You guessed my number")
else:
    print("Better luck next time.")

#SLIDE 33
from datetime import date, time

def print_name():
    name = input("Enter your name: ")
    return name

print("Your name is", print_name())

def print_name2():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    user_number = int(input("Enter a number: "))
    td = date.today()
    user_id = (user_number * age) + td.day
    return "{} your user id is {}".format(name.capitalize(), user_id)

print(print_name2())

#SLIDE 37
def numbers():
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter a number: "))
    number_3 = int(input("Enter a number: "))
    number_4 = int(input("Enter a number: "))
    return number_1 + number_2 + number_3 + number_4

print(numbers())


def numbers2():
    count = 0
    numbers_list = []
    total = 0
    while count < 4:
        number = int(input("Enter a number: "))
        numbers_list.append(number)
        count += 1
    for number in numbers_list:
        total += number
    return total

print("Total = ", numbers2())
