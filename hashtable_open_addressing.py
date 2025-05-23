class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None] * size

    def __repr__(self):
        """returns a formatted string containing the values in the hash table"""
        return f"HashTable {self.values}"

    def _hash(self, key: str) -> int:
        """Computes and returns the initial location for a given key using built-in hash function"""
        return hash(key) % self.size
      
    def _rehash(self, old_location: int) -> int:
        """ Compute and returns the next location for linear probing """
        return (old_location + 1) % self.size

    def setitem(self, key: str, value: dict) -> None:
        """
        """
        start = self._hash(key)
        location = start
        while self.values[location]:
            if self.values[location][0] == key:
                self.values[location] = (key, value)
                return
            location = self._rehash(location)
            if location == start:
                raise Exception("Hashtable is full!")
        self.values[location] = (key, value)
        return

    def getitem(self, key: str) -> 'dict | None':
        """
        """
        start = self._hash(key)
        location = start
        looped = False
        while not looped:
            if self.values[location][0] == key:
                k, val = self.values[location]
                return val
            location = self._rehash(location)
            if location == start:
                looped = True
                raise Exception("Hashtable is full!")

# s= HashTable(5)
# print(s.__repr__())
# s.setitem("a", 3)
# print(s.__repr__())
# s.setitem("a", 5)
# print(s.__repr__())
# s.getitem("a")

import csv 
with open("student_data.csv", 'r') as f:
    data = []
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)
