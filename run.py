from typing import List
from letter import LetterState
from play import Wordle
from colorama import Fore
import random

def main():

    word_list = load_word_list("assets/wordle_five.txt")
    secret = random.choice(list(word_list))
    wordle = Wordle(secret)


    
    while wordle.guess_attempt:
       i = input("\nEnter your guess:")

       if len(i) != wordle.WORD_LENGTH:
           print(Fore.RED + f"Guess must be {wordle.WORD_LENGTH} characters long." + Fore.RESET)
           continue
       
       wordle.attempt(i)
       display(wordle)               

    if wordle.game_over:
        print("You have guessed the word. Congrats")
    else:
        print("You have run out of guesses!")
        print(f"The word was: {wordle.secret}")

def display(wordle: Wordle):
    print("\nResult so far: \n")
    print(f"{wordle.remain_attempts} attempts left.")

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

def game_border(lines: list[str], size: int=9, pad: int=1):
    
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