from game.computer import Computer
from game.console import Console
from game.interface import Interface

class Director:
    """ Will controll and keep track of the entire game
    
        Stereotype: Controller
        
        Attributes:
        computer(Computer)
        console(Console)
        interface(Interface)
        keep_playing(Boolean)
        """

    def __init__(self):
        self.computer = Computer()
        self.console = Console()
        self.interface = Interface()
        self.keep_playing = True

    def first_line(self):
        hidden_word = self.computer.hidden_word()
    
    def star_game(self):

        while self.keep_playing:
            self.get_input()
            self.do_updates()
            self.do_outputs()
    
    def get_input(self):
        hidden_word = self.computer.hidden_word()
