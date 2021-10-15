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
        self.console.print_message(hidden_word)
    
    def start_game(self):
        self.first_line()
        while self.keep_playing:
            self.get_input()
            self.do_updates()
            self.do_outputs()
    
    def get_input(self):
        self.interface.drawing()
        print("^"*7)
        self.computer.letter = self.console.return_input(self.computer.get_message())

    def do_updates(self):
        print(self.computer.comparisson(self.computer.letter))
        if self.computer.check_letter():
            self.interface.delete_line()

    
    def do_outputs(self):
        if self.interface.can_play():
            self.keep_playing = False
            self.interface.drawing()
        
        elif self.computer.comparisson(self.computer.letter) == self.computer.word:
            print('You win!')



