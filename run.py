from letter import LetterState
from play import Wordle
from colorama import Fore
import random

'''
Gameplay adapted using this Youtube tutorial -
https://www.youtube.com/watch?v=SyWeex-S6d0.

'''


def main():

    '''
    Main function of the game. A word from the "wordle_five.txt"using
    https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt
    in the assets folder is picked at randomly using python random.
    '''

    word_list = load_word_list("assets/wordle_five.txt")
    secret = random.choice(list(word_list))
    wordle = Wordle(secret)
    play_game = True

    print("\n---- Welcome to Worldle ----\n")
    print("HOW TO PLAY:\n")
    print("* Type your 5 letter worded guess. At the prompt below.\n")
    print("* If your guess contains a letter in the same position as the"
          " random word. \nIt will highlight in", Fore.GREEN + "Green.\n" +
          Fore.RESET)
    print("* If your guess contains a letter that is in the random word but "
          "not in its \ncurrent position. It will highlight in", Fore.BLUE +
          "Blue.\n" + Fore.RESET)
    print("* If your guess contains a letter that is not in the random word.\n"
          "It will highlight in", Fore.RED + "Red.\n" + Fore.RESET)
    print("You have 6 attempts to guess the game's randomly selected 5 letter"
          " word." "\n GOOD LUCK! \n")
    while play_game is True and wordle.guess_attempt:
        i = input("Enter your guess:")
        i = i.upper()
        if len(i) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Guess must be {wordle.WORD_LENGTH} letters"
                  " long. Guess again." + Fore.RESET)
            # Restrict the guesses to 5 letter words ONLY"
            continue

        if i not in word_list:
            print(Fore.RED + f"{i} is not recognized as a valid word."
                  + Fore.RESET)
            continue
        wordle.attempt(i)
        display(wordle)

    if wordle.game_over:
        print("You have guessed the word. Congrats!")
        # Appears when the word has been guessed successfully.
        print(f"With {wordle.remain_attempts} attempt(s) remaining.")
        user_input = input(f"PLAY AGAIN Y/N:").lower()
        if user_input == "y":
            play_game = True
            main()
        elif user_input == "n":
            print("Goodbye!")
            play_game = False

    else:
        print("You have run out of guesses!")
        print(f"The word was: {wordle.secret}.\n")
        # Tells the player what the word was after attempts are exhausted.
        user_input = input(f"PLAY AGAIN Y/N:").lower()
        if user_input == "y":
            play_game = True
            main()
        elif user_input == "n":
            print("Goodbye!")
            play_game = False


def display(wordle: Wordle):
    print("\nResult so far: \n")
    print(f"{wordle.remain_attempts} attempts left.")
    # Displays the remaining attempts (MAX = 6)

    lines = []

    for word in wordle.guesses:
        result = wordle.guess(word)
        convert_result_str = convert_to_color(result)
        lines.append(convert_result_str)
    for _ in range(wordle.remain_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    game_border(lines)


def load_word_list(path: str):
    word_list = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_list.add(word)
    return word_list


def convert_to_color(result: list[LetterState]):

    '''
    The below function converts the letters in the player's guesses
    into colors.Green if the letter is in the same spot as the random word.
    Blue if its in the word but not in its current position.
    Finally, Red if the letter(s) is not in the word.
    '''

    result_color = []
    for letter in result:
        if letter.is_in_spot:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.BLUE
        else:
            color = Fore.RED
        color_letter = color + letter.character + Fore.RESET
        result_color.append(color_letter)
    return " ".join(result_color)


def game_border(lines: list[str], size: int = 9, pad: int = 1):

    '''
    Creates a box around the 6 guesses using
    https://en.wikipedia.org/wiki/Box-drawing_character
    '''
    length = size + pad * 2
    top = "╔" + "═" * length + "╗"
    bottom = "╚" + "═" * length + "╝"
    space = "" * pad
    print(top)
    for line in lines:
        print("║" + space + line + space + "  ║")
    print(bottom)


if __name__ == "__main__":
    main()
