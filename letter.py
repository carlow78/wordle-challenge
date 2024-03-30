class LetterState:

    def __init__(self, character: str):
        self.character: str = character
        self.is_in_word: bool = False # Letter is in word but not in position
        self.is_in_spot: bool = False # Letter is in word and in the position
    
    # Inbuilt function for representing string
    def __repr__(self):
        return f"[{self.character} is_in_word: {self.is_in_word} is_in_spot: {self.is_in_spot}]"