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