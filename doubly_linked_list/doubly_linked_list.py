"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a node to add
        new_node = ListNode(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
             
            # new_node should point to current head as next
            new_node.next = self.head
            # current head should point to new_node as prev
            self.head.prev = new_node 
            # move head to new node
            self.head = new_node
            # increment list size
            self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list, so
        # save the head_value to be returned
        head_value = self.head.value
        # move adjecent second node to head
        self.head = self.head.next
        # remove prev node reference on new head node
        self.head.prev = None
        return head_value 

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create a node to add
        new_node = ListNode(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next = new_node
            # point new tail node's prev to old tail
            new_node.prev = self.tail
            # point current tail to new node
            self.tail = new_node
            # increment list size
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next is None:
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value
        
        else:
            # otherwise we have more elements in the list
            tail_value = self.tail.value
            # point current tail to old tail previous node
            self.tail = self.tail.prev
            # remove next node reference on new tail node
            self.tail.next = None
            return tail_value 

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            # remove previous node from new head
            node.prev = None
            node.next = self.head.next 
            # move head to new node
            self.head = node 
            
            

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            # remove previous node from new head
            node.prev = self.tail
            node.next = None
            # move head to new node
            self.tail = node 

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if list is empty
        if not self.head and not self.tail:
            # error handling
            return

        self.length -= 1

        # if head and tail are the same
        if self.head is self.tail:
            self.head = None
            self.tail = None

        # If node is head
        elif self.head == node:
        # elif self.head is node:    
            self.head = self.head.next
            node.delete()

        # if node is tail
        elif self.tail == node:
        # elif self.tail is node:    
            self.tail = self.tail.prev
            node.delete()

        else:
            node.delete()

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        
        # check if list is empty
        if self.head is None and self.tail is None:
            return 0

        # check if only one item in list
        if not self.head.next:
            return self.head.value

        # Variable to hold current max
        curr_max = None

        current_node = self.head
        
        while current_node is not None:
           
            # check if current_node value is > then curr_max
            if curr_max is None or current_node.value > curr_max:
                
                curr_max = current_node.value

            current_node = current_node.next

        return curr_max
