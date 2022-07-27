class HashTable:

    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        """Big O: O(1)"""
        # Calculates the location where the item would be stored.

        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        """Big O: O(1)"""
        # Adds an item to the hash table

        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """Big O: O(n)"""
        # Returns a value corresponding to the key provided.

        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        """Big O: O(n)"""
        # Returns all the keys present in the hash table.

        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        """Big O: O(n)"""
        # Prints all the key value pairs in the hash table.
        
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)



my_hastable = HashTable(15)

my_hastable.set_item('nuts', 1200)
my_hastable.set_item('bolts', 200)
my_hastable.set_item('app', 10)

print(my_hastable.get_item('nuts'))
print(my_hastable.get_item('app'))
print(my_hastable.get_item('brhhs'))

print(my_hastable.keys())

# my_hastable.print_table()