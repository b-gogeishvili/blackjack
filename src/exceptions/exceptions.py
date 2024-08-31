class PlayerBusted(Exception):
    """Exception raised if player is busted."""
    def __init__(self, message="Player Busted"):
        self.message = message
        super().__init__(self.message)

class ComputerBusted(Exception):
    """Exception raised if computer is busted."""
    def __init__(self, message="Computer Busted"):
        self.message = message
        super().__init__(self.message)
