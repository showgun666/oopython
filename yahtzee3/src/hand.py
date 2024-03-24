"""
class Hand:
"""
from src.die import Die
class Hand:
    """class Hand:"""
    def __init__(self, dice_values=None):
        if dice_values is None:
            self.dice = [Die() for _ in range(5)]
        else:
            self.dice = [Die(value) for value in dice_values]

    def roll(self, indexes=None):
        """
        kastar tärningar
        """
        if indexes is None:
            for die in self.dice:
                die.roll() #kasta alla tärningar
        else:
            for index in indexes:
                self.dice[index].roll()

    def __str__(self):
        """
        retunera namn på tärningar med "," separerad
        """
        return ", ".join(str(die) for die in self.dice)

    def to_list(self):
        """
        Returnerar en lista som innehåller värdet av varje tärning i handen.
        """
        value_list = []
        for die in self.dice:
            value_list.append(die.get_value())
        return value_list
