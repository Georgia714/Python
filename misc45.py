

def favourite_meal():
    starter = input("Enter your favourite starter: ")
    main = input("Enter your favourite main course: ")
    dessert = input("Enter your favourite dessert: ")
    drink = input("Enter your favourite drink: ")
    print("Your favourite meal is {}, followed by {}, then {} with a glass of {}.".format(starter.lower(), main.lower(), dessert.lower(), drink.lower()))

favourite_meal()


motorbike_cost = 2000
number_years = 0
while motorbike_cost > 1000:
    motorbike_cost = motorbike_cost * 0.9
    number_years += 1

print("Motorbike cost after {} years = £{:.2f}".format(number_years, motorbike_cost))

favourite_number = int(input("Enter your favourite number: "))

def joke(number):
    if number > 10:
        joke = "Why don't you ever see Father Christmas in hospital?"
        answer = "Because he has private elf-care."
    else:
        joke = "Why did the two penguins jump when they first met?"
        answer = "They were trying to break the ice."
    print("{}\n{}".format(joke, answer))

joke(favourite_number)
