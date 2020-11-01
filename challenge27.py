word = ""

while len(word) < 4:
    word = input("Player 1, enter a five-letter word: ")

answer = list(word)
answer_hidden = []
answer_hidden.extend(answer)
#print(answer)
for i in range(len(answer_hidden)):
    answer_hidden[i] = "*"

print("Word to guess:"," ".join(answer_hidden))

number_guesses = 0

while number_guesses < len(answer):
    guess = input("Player 2: Guess the word, enter a letter: ")
    guess = guess.lower()
    if guess not in answer:
        print("Incorrect letter. Guess again.")
        number_guesses += 1
    for i in range(len(answer)):
        if answer[i] == guess:
            answer_hidden[i] = guess
            print("Correct letter", answer_hidden)
            number_guesses += 1

print(answer_hidden)
if answer_hidden == answer:
    answer = ''.join(answer)
    print("You guessed it! The answer is:", answer.capitalize())
else:
    print("You're out of guesses. Unlucky, next time.")
#https://www.youtube.com/watch?v=jPmBUoSZ6tY
#        if letter == word[i]:
#            print(word[:i])
#            lives -= 1
#        else:
#            print("Guess again")
#            print(letter)
#            lives -= 1
