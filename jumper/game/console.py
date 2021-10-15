class Console:
    """Get the text and display outputs
    
    Attributes:
    prompt (string): prompt to display on each line"""

    def return_input(self, prompt):
        return input(prompt)

    def print_message(self, message):
        print(message)