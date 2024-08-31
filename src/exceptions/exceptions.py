class PlayerBusted(Exception):
    """Exception raised if player is busted."""
    def __init__(self, message="---- Player Busted\n"):
        self.message = message
        super().__init__(self.message)

class ComputerBusted(Exception):
    """Exception raised if computer is busted."""
    def __init__(self, message="---- Computer Busted\n"):
        self.message = message
        super().__init__(self.message)
