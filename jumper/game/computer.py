import random

class Computer:

    """Will select the word from the list, will ask the guesser 
    for a letter and compute the result
    
       Stereotype: Information holder
       
       Attributes: 
        - words(list): Contains the words for the game
        - letter(string): The letter from the guesser
        - word(string): It will store the selected word from words"""

    def __init__(self):
        """Constructor of the class
        Argument: self (Computer)"""
        self.words = ["dog", "cat", "hamburger", "dinosaur", "tiger"]
        self.letter = ""
        self.word = random.choice(self.words)
        
    
    def hidden_word(self):
        """Will hide the selected word according to its length
        
        Argument: self(Computer)"""

        word = self.word
        hidden_word = ""
        for i in word:
            hidden_word += "_"
        return hidden_word

    def comparisson(self, received_letter):
        """Will check if the letter guessed is in the word

        Argument: 
        self(Computer)
        received_letter(The guessed letter)
        """
        word = self.word
        new_hidden_word = ""
        for i in word:
            if received_letter == i:
                new_hidden_word += i
            else:
                new_hidden_word += "_"   
        return new_hidden_word

    

    
    def get_message(self):
        """ Get the message from the player"""

        message = "\n Guess a letter (a-z): "
        return message
        