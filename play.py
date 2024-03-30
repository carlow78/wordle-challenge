from run import Wordle

def main():
    wordle = Wordle("TAXES")
    
    while wordle.guess_attempt:
       x = input("Enter your guess:\n")
       wordle.attempt(x) 

    if wordle.game_over:
        print("You have guessed the word. Congrats")
    else:
        print("You have run out of guesses!")


if __name__ == "__main__":
    main()