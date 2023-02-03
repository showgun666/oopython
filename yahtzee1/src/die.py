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
    def __init__(self, _value=None):
        if _value is None:
            self._value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
        elif _value < Die.MIN_ROLL_VALUE:
            self._value = Die.MIN_ROLL_VALUE
        elif _value > Die.MAX_ROLL_VALUE:
            self._value = Die.MAX_ROLL_VALUE
        else:
            self.value = value
    def get_name(self, _value):
        """
        get name from value:
        """
        if _value == 1:
            self._value = "one"
        elif _value == 2:
            self._value = "two"
        elif _value == 3:
            self._value = "three"
        elif _value == 4:
            self._value = "four"
        elif _value == 5:
            self._value = "five"
        else:
            self._value = "six"
    def get_value(self):
        """
        Return the value of the Die
        """
        return self._value
    def roll(self):
        """
        Method att kasta tärningar som retunerar värde mellan 1 och 6
        """
        self._value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
    def __str__(self):
        """
        konvertera till string
        """
        return str(self._value)
        