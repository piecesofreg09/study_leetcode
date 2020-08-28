'''
using hash map to store data
{0:1, 1:1, 2:1, 3:2, 4:3, 5:2}
using hash map set to store reverse
{1:{0,1,2},
2:{3,5},
3:{4}}

when delete, move the last element to the deleted location
that is if we are deleting 3 at 4, we move 2 at 5 to 2 at 4
final result will be 
{0:1, 1:1, 2:1, 3:2, 4:2}
{1:{0,1,2},, 2:{3,4}, 3:{}} -> further down to be -> {1:{0,1,2},, 2:{3,4}, 3:{}}
that is if we are deleting 2 at 5, we remove 2 at 5 easy
final result will be
{0:1, 1:1, 2:1, 3:2, 4:2}
{1:{0,1,2},, 2:{3}, 3:{4}}
pop from set is O(1)
del from hashmap is O(1)
'''

import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.reverse_map = {}
        self.count = 0
        self.last_element = None

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        cur = self.count
        self.data[cur] = val
        if val in self.reverse_map:
            self.reverse_map[val].add(cur)
        else:
            self.reverse_map[val] = set([cur])
        self.count += 1
        self.last_element = self.data[self.count - 1]
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        #print(self.reverse_map)
        #print(self.count)
        if self.count == 0:
            return False
        self.last_element = self.data[self.count - 1]
        if val in self.reverse_map:
            if val == self.last_element:
                self.reverse_map[self.last_element].remove(self.count - 1)
                del self.data[self.count - 1]
                if len(self.reverse_map[val]) == 0:
                    del self.reverse_map[val]
                self.count -= 1
            else:
                self.reverse_map[self.last_element].remove(self.count - 1)
                #print(self.reverse_map)
                temp = self.reverse_map[val].pop()
                if len(self.reverse_map[val]) == 0:
                    del self.reverse_map[val]
                self.reverse_map[self.last_element].add(temp)
                self.data[temp] = self.last_element
                self.count -= 1
            return True
        return False
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        x = random.randrange(self.count)
        return self.data[x]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
