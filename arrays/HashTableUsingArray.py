"""
Worst Case Runtime : O(N)
Best Case Runtime : O(1)
"""
from utilities.LinkedList import LinkedList


class HashTableUsingArray:

    def __init__(self, size):
        self.size = size
        self.hash_table = [None]*size

    def __repr__(self):
        return str(self.hash_table)

    def insert(self, data):
        bucket = self.bucket(data)
        if self.hash_table[bucket] is None:
            ll = LinkedList()
            ll.add_element(data)
            self.hash_table[bucket] = ll
        else:
            self.hash_table[bucket].add_element(data)

    def bucket(self, data):
        return hash(data)%self.size



