print("Hello! Welcome to Hangman!")
word = input("What is the word? ")

def hangman(word):
    hidden_word = "-" * len(word)
    print("This is the hidden word " + hidden_word)
    user_input = input("Guess a letter: ")
    if user_input in word:
        occurences = findOccurrences(word, user_input)
        for index in occurences:
            hidden_word = hidden_word[:index] + user_input + hidden_word[index + 1:]
        print(hidden_word)
    else:
        user_input = input("Sorry that letter was not found, please try again: ")

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

    hangman("Hello!")
    Input("Guess a letter: ")
    if user_input in word:
        occurences = findOccurrences(word, user_input)
        for index in occurences:
            hidden_word = hidden_word[:index] + user_input + hidden_word[index + 1:]
        print(hidden_word)
    else:
        user_input = input("Sorry that letter was not found, please try again: ")

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

hangman("Hello!")