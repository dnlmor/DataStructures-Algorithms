class Array:
    def __init__(self):
        self.array = []
    
    def insert(self, value):
        """Inserts an element at the end of the array."""
        self.array.append(value)

    def delete(self, value):
        """Deletes the first occurrence of the element from the array."""
        if value in self.array:
            self.array.remove(value)
    
    def search(self, value):
        """Returns the index of the element if found, otherwise -1."""
        try:
            return self.array.index(value)
        except ValueError:
            return -1

    def traverse(self):
        """Prints each element in the array."""
        for item in self.array:
            print(item)
