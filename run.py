
class Wordle:

    MAX_GUESSES = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
        self.secret: str = secret
        self.guesses = []
        pass

    def attempt(self, word: str):
        self.guesses.append(word)

    # Function when the word has been guessed correctly. Game over.

    @property # Allows us to call the function without ()
    def game_over(self):
        return len(self.guesses) > 0 and self.guesses[-1] == self.secret
    
    # Function for remaining attempts
    @property
    def remain_attempts(self) -> int:
       return self.MAX_GUESSES - len(self.guesses)

    
    # Function to allow player only 5 guesses
    
    @property 
    def guess_attempt(self):
        return self.remain_attempts > 0 and not self.game_over
    

