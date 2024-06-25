from .ops import Operations

class Player(Operations):
    def __init__(self) -> None:
        super().__init__()
        self.username = "Pug"
        self.cash = 500
