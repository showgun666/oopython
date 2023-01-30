"""
Class Die:
"""
import random
class Die:
    """
    Class die som inehåller defoult värde MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    def __init__(self, value=None):
        if value is None:
            self.value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
        elif value < Die.MIN_ROLL_VALUE:
            self.value = Die.MIN_ROLL_VALUE
        elif value > Die.MAX_ROLL_VALUE:
            self.value = Die.MAX_ROLL_VALUE
        else:
            self.value = value
    def get_name(self, value):
        """
        get name from value:
        """
        if value == 1:
            self.value = "one"
        elif value == 2:
            self.value = "two"
        elif value == 3:
            self.value = "three"
        elif value == 4:
            self.value = "four"
        elif value == 5:
            self.value = "five"
        else:
            self.value = "six"
    def get_value(self):
        """
        Return the value of the Die
        """
        return self.value
    def roll(self):
        """
        Method att kasta tärningar som retunerar värde mellan 1 och 6
        """
        self.value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
    def __str__(self):
        """
        konvertera till string
        """
        return str(self.value)
        