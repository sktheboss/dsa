"""
This implementation defines a Node class to represent a single node in the linked list,
and a CircularLinkedList class to represent the linked list itself. 
The CircularLinkedList class has methods for appending an element to the end of the list.
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node
    
    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail.next = self.head.next
                self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next != self.head:
                if current_node.next.data == data:
                    if current_node.next == self.tail:
                        current_node.next = self.head
                        self.tail = current_node
                    else:
                        current_node.next = current_node.next.next
                    return
                current_node = current_node.next
    
    def __len__(self):
        if self.head is None:
            return 0
        current_node = self.head
        count = 1
        while current_node.next != self.head:
            count += 1
            current_node = current_node.next
        return count
    
    def __repr__(self):
        if self.head is None:
            return '[]'
        current_node = self.head
        result = '[' + str(current_node.data)
        while current_node.next != self.head:
            current_node = current_node.next
            result += ', ' + str(current_node.data)
        result += ']'
        return result

# Example usage
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print(cll) # prints [1, 2, 3]
cll.prepend(0)
print(cll) # prints [0, 1, 2, 3]
print(len(cll)) # prints 4
cll.remove(2)
print(cll) # prints [0, 1, 3]
