"""
En abstrakt klass som representerar en regel i yahtzee.
För varje sätt att få poäng existerar en underklass.
"""
from abc import ABC, abstractmethod

class Rule(ABC):
    @abstractmethod
    def points(self, hand):
        pass

class ThreeOfAKind(Rule):
    " Rule for counting points for the three of a kind rule."
    def __init__(self):
        self.name = "Three of a Kind"

    def points(self, hand):
        " Returns the sum of the hand's values if a triple value exists."
        # Make a list of the values
        values = hand.to_list()
        value_dic = {}
        # Loop through values and count unique values in a dictionary
        for value in values:
            if value not in value_dic:
                value_dic[value] = 1
            else:
                value_dic[value] += 1
        # Enumerate through dictionary, return sum of values if a dic value is 3 or higher
        for _, value in enumerate(value_dic):
            if value_dic[value] >= 3:
                return sum(values)

class FourOfAKind(Rule):
    " Rule for counting points for the four of a kind rule."
    def __init__(self):
        self.name = "Four of a Kind"

    def points(self, hand):
        " Returns the sum of the hand's values if a triple value exists."
        # Make a list of the values
        values = hand.to_list()
        value_dic = {}
        # Loop through values and count unique values in a dictionary
        for value in values:
            if value not in value_dic:
                value_dic[value] = 1
            else:
                value_dic[value] += 1
        # Enumerate through dictionary, return sum of values if a dic value is 4 or higher
        for _, value in enumerate(value_dic):
            if value_dic[value] >= 4:
                return sum(values)

class FullHouse(Rule):
    " Rule for counting values for the Full House rule."
    def __init__(self):
        self.name = "Full House"
    
    def points(self, hand):
        " Returns 5 points if hand contains a double value and a triple value."
        # Make a list of the values
        values = hand.to_list()
        value_dic = {}
        # Flags for doubles and triples
        doubles = False
        triples = False
        # Loop through values and count unique values in a dictionary
        for value in values:
            if value not in value_dic:
                value_dic[value] = 1
            else:
                value_dic[value] += 1
        # Enumerate through dictionary, switch flags if double or triple exists.
        for key, value in enumerate(value_dic):
            if value_dic[value] == 3:
                triples = True
            elif value_dic[value] == 2:
                doubles = True
        # If both flags are True, return 25 points.
        if triples and doubles:
            return 25

class SmallStraight(Rule):
    " Rule for counting values for the Small Straight rule."
    def __init__(self):
        self.name = "Small Straight"
    
    def points(self, hand):
        # Get a list of values from hand.
        values = hand.to_list()
        # Sort the list and remove duplicates.
        values = sorted(set(values))

        # Loop through list and see if it has 4 numbers in a sequence.
        # Restrict the indexes by length of values.
        # Loop through each value in
        for i in range(len(values)-3):
            # Control if the difference between the value in current index and index+3 is 3.
            if values[i+3] - values[i] == 3:
                return 30


class SameValueRule(Rule):
    """
    Parent Class for rules counting same values.
    """
    def __init__(self, value, name):
        self.value = value
        self.name = name
    def points(self, hand):
        """
        Returns the sum of values in hand equal to self.value
        """
        # Create list of values from hand object.
        values = hand.to_list()
        points = 0
        # Loop through values and increment points by every valid value.
        for value in values:
            if self.value == value:
                points += value
        return points

class Ones(SameValueRule):
    " Child class for counting ones. "
    def __init__(self):
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    " Child class for counting twos. "
    def __init__():
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    " Child class for counting threes. "
    def __init__():
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    " Child class for counting fours. "
    def __init__():
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    " Child class for counting fives. "
    def __init__():
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    " Child class for counting sixes. "
    def __init__():
        super().__init__(6, "Sixes")
