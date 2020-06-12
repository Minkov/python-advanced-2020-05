class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f'Name: {self.name}, Mark: {self.mark}'

    def __repr__(self):
        return f'Name: {self.name}, Mark: {self.mark}'