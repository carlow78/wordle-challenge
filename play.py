from letter import LetterState

class Wordle:

    MAX_GUESSES = 6
    WORD_LENGTH = 5
 

    def __init__(self, secret: str):
        self.secret: str = secret.upper() # capitalizes the player's guess
        self.guesses = []
        pass

    def attempt(self, word: str):
        word = word.upper() 
        self.guesses.append(word)
   

    def guess(self, word: str):
        word = word.upper()
        result = []

# Checks to see if any letter in the player's are within the randomly selected word.
        
        for x in range(self.WORD_LENGTH):
            character = word[x]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_spot = character == self.secret[x]
            result.append(letter)
            
        return result

    # Function when the word has been guessed correctly. Game over.

    @property # Allows us to call the function without ()
    def game_over(self):
        return len(self.guesses) > 0 and self.guesses[-1] == self.secret
    
    # Function for remaining attempts
    @property
    def remain_attempts(self) -> int:
       return self.MAX_GUESSES - len(self.guesses)


    # Function to allow player only 6 guesses (MAX_GUESSES)
    @property 
    def guess_attempt(self):
        return self.remain_attempts > 0 and not self.game_over
    

