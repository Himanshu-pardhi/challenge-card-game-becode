class Symbol:
    def __init__(self,color,icon)->str:
        self.colors = color 
        self.icons = icon

#class Card created inherits from class symbol
class Card(Symbol):
    def __init__(self,color,icon,value):
        super().__init__(color,icon)
        self.values = value

#fun to create on cards
    def __str__(self):
        return f"{self.colors},{self.icons},{self.values}"

card = Card("Black","♣","0") 
print(card)