class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = Node('dummy')
        self.size = 0
        
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        else:
            cur = self.dummy
            count = 0
            while count < index:
                cur = cur.next
                count += 1
            
            return cur.next.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val=val)
        tempHead = self.dummy.next
        self.dummy.next = newNode
        newNode.next = tempHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val=val)
        
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = newNode
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        elif index < self.size:
            cur = self.dummy
            count = 0
            while count < index:
                cur = cur.next
                count += 1
            newNode = Node(val=val)
            temp = cur.next
            cur.next = newNode
            newNode.next = temp
            
            self.size += 1
            
        else:
            self.addAtTail(val)
         
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        else:
            cur = self.dummy
            count = 0
            while count < index:
                cur = cur.next
                count += 1
            cur.next = cur.next.next
            
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
