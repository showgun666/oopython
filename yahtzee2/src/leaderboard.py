"""
Denna modul innehåller klassen leaderboard som innehåller en unordered list
Leaderboard hanterar hur data lagras och hämtas från unordered list.
"""
from src.unorderedList import UnorderedList
class Leaderboard():
    """ Leaderboard class """
    def __init__(self, entries=None):
        self.entries = UnorderedList()
        for i in entries:
            self.entries.append(i)

    @classmethod
    def load(cls, filename):
        """
        Read data from file filename.
        Returns a new leaderboard object filled with data from file.
        """
        instance = cls()
        with open(filename, "r") as f:
            for line in f:
                name, score = line.split(";")
                instance.add_entry(name, score)
        return instance
    
    def save(self, filename):
        """
        Saves data from entries to file filename.
        """
        with open(filename, "w") as f:
            print(self.entries.print_list(), file=f)

    def add_entry(self, name, score):
        """
        Appends a name and score to entries.
        """
        self.entries.append(("%s;%s" % (name, score)))

    def remove_entry(self, index):
        """
        Removes an entry from entries with the value of index.
        """
        self.entries.remove(index)
