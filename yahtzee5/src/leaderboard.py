"""
Denna modul innehåller klassen leaderboard som innehåller en unordered list
Leaderboard hanterar hur data lagras och hämtas från unordered list.
"""
from src.unorderedList import UnorderedList

class Leaderboard():
    """ Leaderboard class """
    def __init__(self, entries=None):
        self.entries = UnorderedList()
        if entries:
            for i in entries:
                self.entries.append(i)

    @classmethod
    def load(cls, filename):
        """
        Read data from file filename.
        Returns a new leaderboard object filled with data from file.
        """
        instance = cls()
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    name, score = line.split(";")
                    instance.add_entry(name, score)
        return instance

    def save(self, filename):
        """
        Saves data from entries to file filename.
        """
        with open(filename, "w", encoding="utf-8") as f:
            i = 0
            while i < len(self):
                string = str(self[i][0]) + ";" + self[i][1] + "\n"
                string.strip()
                if string:
                    f.write(string)
                i += 1

    def add_entry(self, name, score):
        """
        Appends a name and score to entries.
        """
        self.entries.append(((name, score)))

    def remove_entry(self, index):
        """
        Removes index from entries.
        """
        self.entries.remove(self[index])

    def __len__(self):
        return self.entries.size()

    def __str__(self):
        return self.entries.print_list()

    def __getitem__(self, key):
        return self.entries.get(key)

    def __setitem__(self, key, value):
        self.entries.set(key, value)
