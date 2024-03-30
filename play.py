from run import Wordle

def main():
    wordle = Wordle("APPLE")
    
    while wordle.guess_attempt:
       i = input("Enter your guess:")
       wordle.attempt(i)
       result = wordle.guess(i)
       print(*result, sep="\n")

    if wordle.game_over:
        print("You have guessed the word. Congrats")
    else:
        print("You have run out of guesses!")


if __name__ == "__main__":
    main()