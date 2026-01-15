# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ''.join(char if char in guesses else '_' for char in secret_word)
        print(display)
        all_guessed = all(char in guesses for char in secret_word) # loop over secret_word
        return all_guessed
    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter secret word: ").lower()
    game = make_hangman(secret_word)
    print("Let's Play!")

    while True:
        guess = input("Guess a letter: ").lower()
        finished = game(guess)
        if finished:
            print(f"Congratulation! You've guessed the word")
            break



