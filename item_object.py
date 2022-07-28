class Item:
    name = ''
    pieces = 0
    amount_of_pieces = 0
    def __init__(self, name, pieces, amount_of_pieces):
        self.name = name
        self.pieces = pieces
        self.amount_of_pieces = amount_of_pieces

    def changeName(self):
        pi = input("Chnage the name: ")
        self.name = pi

    def changePieces(self):
        pi = int(input("Change pieces: "))
        self.pieces = pi
    
    def changePiecesAmount(self):
        pi = int(input("Change the amount of pieces: "))