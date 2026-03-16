#Task-5 Hash Table
#Task: Use AI to implement a hash table with basic insert, search, and delete methods.
#Sample Input Code:class HashTable:pass
#Expected Output:Collision handling using chaining, with well-commented methods.
class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                return v
        return "Not Found"


ht = HashTable()

ht.insert(1, "Apple")
ht.insert(2, "Banana")

print("Search key 1:", ht.search(1))
print("Hash Table:", ht.table)