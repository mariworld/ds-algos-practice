class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None
    def __str__(self):
        return f"{self.val}"
    
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def __str__(self):
        return f"{self}"

new_node = Node(50)
sll1 = SinglyLinkedList()
sll1.push(new_node)
next_node = Node(12)
sll1.push(next_node)
last_node = Node(79)
sll1.push(last_node)
print(sll1)