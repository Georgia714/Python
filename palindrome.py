#This program asks the user to enter a word and checks if it is a palindrome.

def palindrome(word = input("enter a word: ")):
    word_backwards = word[::-1]
    if word.lower() == word_backwards.lower():
        palindrome = True
        print("That's a palindrome.")
    else:
        palindrome = False
        print("That's not a palindrome.")

palindrome()
