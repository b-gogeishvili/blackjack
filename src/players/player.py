from .ops import Operations

class Player(Operations):
    def __init__(self, name, cash) -> None:
        super().__init__("Player")
        self.username = name
        self.cash = cash
