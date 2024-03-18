import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "pear", "grape", "kiwi", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def main():
    print("Welcome to the Word Guessing Game!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's start the game.")
    
    word_to_guess = choose_word()
    guessed_letters = []
    turns = 12
    
    while turns > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Correct!")
        else:
            print("Incorrect!")
            turns -= 1
        
        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    
    if turns == 0:
        print("\nOops! You ran out of turns. The word was:", word_to_guess)

if __name__ == "__main__":
    main()
