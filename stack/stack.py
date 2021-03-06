class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None # Stores a node, that corresponds to our first node in the list 
        self.tail = None # stores a node that is the end of the list
  
    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value 

    def contains(self, value):
        if self.head is None:
            return False
        
        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head
    
        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True
    
            # otherwise, go to the next node
            current_node = current_node.next_node
        return False 
  
    def get_max(self):

        # Variable to hold current max
        curr_max = 0

        current_node = self.head
        
        while current_node is not None:
            # check if current_node value is > then curr_max
            if current_node.value > curr_max:
                
                curr_max = current_node.value

            current_node = current_node.next_node

        if curr_max == 0:
            return None
        else:
            return curr_max


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        # return len(self.storage)
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)

        self.size += 1

    def pop(self):
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     return self.storage.pop()
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()
