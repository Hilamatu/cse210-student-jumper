class Interface:
    """ Will create and display the items for interface
    
        Stereotype: interface
        
        Attributes:
        parachute(list): the parts of the parachute
         """""

    def __init__(self):
        """Class constructor"""
        self.parachute = ["  ___", " /___\\", " \   /", "  \ /", "   0", "  /|\\", "  / \\"]    

    def drawing(self):
        """Will draw the parachute
        
        Argument: self(Computer)"""
        for i in self.parachute:
            print(i)
    
    def delete_line(self):

        """Will delete one line of the parachute if the player 
        gusses wrong.
        
        Argument: self(Computer)"""

        self.parachute.pop(0)

    