from letter import LetterState

class Wordle:

    MAX_GUESSES = 6
    WORD_LENGTH = 5
    VOID_LETTER = "*"
 

    def __init__(self, secret: str):
        self.secret: str = secret.upper() # capitalizes the player's guess
        self.guesses = []
        


    def attempt(self, word: str):
        word = word.upper() 
        self.guesses.append(word)
   
    '''
    The following check for green letters first, then loops again to check for blue letters. 
    '''

    def guess(self, word: str):
        word = word.upper()
        result = [LetterState(i) for i in word]
        remaining_secret = list(self.secret) # copy of list for duplicated letters

        for x in range(self.WORD_LENGTH):
            letter = result[x]
            if letter.character == remaining_secret[x]:
                letter.is_in_spot = True
                remaining_secret[x] = self.VOID_LETTER
      
        for x in range(self.WORD_LENGTH):
            letter = result[x]
           
            if letter.is_in_spot:
                continue
            
            for y in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[y]:
                    remaining_secret[y] = self.VOID_LETTER
                    letter.is_in_word = True
                    break

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
    

