from phrase import Phrase
import random
import sys


class Game:
    def __init__(self):
        self.missed_guesses = 5
        self.maximum_guesses = 5
        self.phrases = [
            Phrase("it takes one to know one"),
            Phrase("the apple of my eye"),
            Phrase("hair of the dog"),
            Phrase("a frog in my throat"),
            Phrase("fly by the seat of your pants")
                       ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return random_phrase

    def welcome(self):
        print("*" * 50)
        name = input("Hello! What is your name?  ")
        print(f"Hello, {name}! Welcome to Phrase Hunter!")
        print("*" * 50)

    def start(self):
        self.welcome()
        while self.missed_guesses > 0 and not self.active_phrase.check_complete(self.guesses):
            print(f"You have {self.missed_guesses} out of {self.maximum_guesses} guesses left.")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            if user_guess in self.guesses:
                print("Oops, you already guessed that letter. Try again.")
            else:
                self.guesses.append(user_guess)
                self.active_phrase.check_guess(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    self.missed_guesses -= 1
        self.game_over()

    def get_guess(self):
        user_input = input("\nPlease guess a letter:  ")
        if len(user_input) > 1:
            print("Invalid entry. Your entry must not be longer than 1 letter.")
        elif not user_input.isalpha():
            print("Invalid entry. Your entry must not contain numbers, digits or punctuation.")
        return user_input

    def game_over(self):
        if self.missed_guesses == 0:
            print("Oh no! Looks like you're out of guesses. Better luck next time!")
        else:
            print("Congratulations! You guessed the phrase!")
            print(self.active_phrase.display(self.guesses))

    def play_again(self):
        would_you_like_to_play_again = input("Would you like to play again? Y/N:  ")
        if would_you_like_to_play_again.upper() == "Y":
            self.start()
        else:
            print("Ok, thanks for playing!")
            sys.exit()






