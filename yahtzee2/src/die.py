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
            self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        elif value < self.MIN_ROLL_VALUE:
            self._value = self.MIN_ROLL_VALUE
        elif value > self.MAX_ROLL_VALUE:
            self._value = self.MAX_ROLL_VALUE
        else:
            self._value = value
    def get_name(self):
        """
        get name from value:
        """
        # Check value of die and return value as one word string.
        if self.get_value() == 1:
            name = "one"
        elif self.get_value() == 2:
            name = "two"
        elif self.get_value() == 3:
            name = "three"
        elif self.get_value() == 4:
            name = "four"
        elif self.get_value() == 5:
            name = "five"
        else:
            name = "six"
        return name
    def get_value(self):
        """
        Return the value of the Die
        """
        return self._value
    def roll(self):
        """
        Method att kasta tärningar som retunerar värde mellan 1 och 6
        """
        self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
    def __str__(self):
        """
        konvertera till string
        """
        return str(self._value)

    def __eq__(self, die):
        """
        Argumentet die är antingen en instans av die eller int.

        Om argumentet die ger samma värde som som objektet
        som använder metoden så returneras True.
        Annars False.

        Metoden kan ta ett argument som inte är die eller int,
        men returnerar då False
        """
        if isinstance(die, int):
            return self.get_value() == die
        if isinstance(die, Die):
            return self.get_value() == die.get_value()
        return False
