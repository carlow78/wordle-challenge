class LetterState:

    def __init__(self, character: str):
        self.character: str = character
        self.is_in_word: bool = False # Letter is in word but not in position
        self.is_in_spot: bool = False # Letter is in word and in the position
    