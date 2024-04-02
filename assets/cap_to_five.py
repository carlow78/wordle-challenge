'''
Keeping script file for reference ONLY. Letters for game now drawn from 
https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt
The function of this script file is to reduce the words in this file -
(https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-medium.txt).
Which contains 5-8 letter words to just the 5 letter words.
First it reads (r) the contents.
And then writes (w) the results to wordle_five.txt.
The total amount of 1367 words will be used for the game.
'''


def main():

    input_file_path = "assets/word.txt"
    output_file_path = "assets/wordle_five.txt"
    five_in_words = []

    with open(input_file_path, "r") as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 5:
                five_in_words.append(word)

    with open(output_file_path, "w") as f:
        for word in five_in_words:
            f.write(word + "\n")

    print(f"Total number of five letter words = {len(five_in_words)}")


if __name__ == "__main__":
    main()
