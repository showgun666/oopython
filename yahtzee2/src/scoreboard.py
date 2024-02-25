"""
Denna modul innehåller en klass som innehåller hur många poäng spelaren
har samlat på sig och vilka regler som spelaren har fått poäng för.
"""
import src.rules as r

class Scoreboard():
    " Class for scoring Yahtzee game. "
    # Initialize the object
    def __init__(self):
        self.rules_list = [
            r.Ones(),
            r.Twos(),
            r.Threes(),
            r.Fours(),
            r.Fives(),
            r.Sixes(),
            r.ThreeOfAKind(),
            r.FourOfAKind(),
            r.FullHouse(),
            r.SmallStraight(),
            r.LargeStraight(),
            r.Yahtzee(),
            r.Chance()
        ]
        self._rules = {
            "Ones": -1,
            "Twos": -1,
            "Threes": -1,
            "Fours": -1,
            "Fives": -1,
            "Sixes": -1,
            "Three Of A Kind": -1,
            "Four Of A Kind": -1,
            "Full House": -1,
            "Small Straight": -1,
            "Large Straight": -1,
            "Yahtzee": -1,
            "Chance": -1,
            }

    # Getter method for the rules
    def get_rules(self):
        " Getter method for the rules"
        return self._rules

    # Get total points accrued by player
    # return int
    def get_total_points(self):
        " Method to get total points accumulated by scoreboard as an integer. "
        rules = self.get_rules()
        total_points = 0

        for i in rules.values():
            if i[0] < 0:
                continue
            total_points += i[0]

        return total_points


    # Add points to the scoreboard based on rule and hand
    # Setter method for the rules attribute
    # If points have already been added based on the specific rule:
    # Raise a ValueError and reward no points.
    # Variables:
    # rule_name : string
    # hand : Hand object
    # Return void
    def add_points(self, rule_name, hand):
        " Method to add points to the scoreboard for a given hand and rule. "
        rules = self.get_rules()

        if self.get_points(rule_name) != -1:
            raise ValueError(f"Points already added for {rule_name}.")

        points = rules[rule_name][1].points(hand)
        if points != 0:
            self._rules[rule_name][0] = points

    # Get points based on rule name
    # Show how many points the player has been rewarded for a specific rule
    # If points have not been rewarded for a specific rule, return -1
    # Variables:
    # rule_name : string
    # Return int, points or -1
    def get_points(self, rule_name):
        " Get points based on rule name. "
        rules = self.get_rules()

        return rules[rule_name][0]

    # Determine if finished
    # If all rules have been used to reward points, return True
    # Return boolean
    def finished(self):
        " Method to determine if all rules have been scored. "
        done_flag = True
        rules = self.get_rules()

        for rule in rules.values():
            if rule[0] < 0:
                done_flag = False
                break
        return done_flag

    # Classmethod to create a new Scoreboard object
    # Variables:
    # points : dictionary with key rule, value points (value rewarded or -1 for unused rule)
    # Return Scoreboard object
    @classmethod
    def from_dict(cls, points):
        " Create a new scoreboard object from a dictionary. "
        instance = cls()
        for key in points.keys():
            instance._rules[key][0] = points[key]

        return instance
