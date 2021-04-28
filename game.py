from phrase import Phrase
import random
import sys

class Game:
    def __init__(self):
        self.num_of_guesses = 5
        self.maximum_guesses = 5
        self.num_games_played = 0
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
        if self.num_games_played == 0:
            self.welcome()
        while self.num_of_guesses > 0 and not self.active_phrase.check_complete(self.guesses):
            print(f"You have {self.num_of_guesses}" + "/" + f"{self.maximum_guesses} guesses left.")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            if user_guess in self.guesses:
                print("*" * 3, "Oops, you already guessed that letter. Try again.", "*" * 3)
            else:
                self.guesses.append(user_guess)
                self.active_phrase.check_guess(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    if len(user_guess) == 1 and user_guess.isalpha():
                        print("*" * 3, "Oops, looks like that letter is not in the phrase.", "*" * 3, "\n")
                        self.num_of_guesses -= 1
                else:
                    print("*" * 3, "Nice work! That letter is in the phrase.", "*" * 3, "\n")
        self.game_over()
        self.play_again()

    def get_guess(self):
        user_input = input("\nPlease guess a letter (to quit, type 'quit'):  ").lower()
        if user_input == "quit":
            sys.exit()
        elif len(user_input) > 1:
            print("Invalid entry. Your entry must not be longer than 1 letter.")
        elif not user_input.isalpha():
            print("Invalid entry. Your entry must not contain numbers, digits or punctuation.")
        return user_input

    def game_over(self):
        self.num_games_played += 1
        if self.num_of_guesses == 0:
            print("Oh no! Looks like you're out of guesses. Better luck next time!")
        else:
            self.active_phrase.display(self.guesses)
            print("\n")
            print("*" * 10, "Congratulations! You guessed the phrase!", "*" * 10)


    def play_again(self):
        while True:
            would_you_like_to_play_again = input("\nWould you like to play again? Y/N:  ")
            if would_you_like_to_play_again.upper() == "Y":
                self.reset_game()
                self.start()
            else:
                print("Ok, thanks for playing!")
                break

    def reset_game(self):
        self.num_of_guesses = 5
        self.maximum_guesses = 5
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]






