class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"node: {self.value}, left: {self.left}, right: {self.right}"

class BinarySearchTree():
    def __init__(self):
        self.root = None
       
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        else:
            print("hits else")
            current = self.root
            while True:
                if new_node.value > current.value:
                    if current.right == None:
                        current.right = new_node
                        return self
                    else:
                        current = current.right
                elif new_node.value < current.value:
                    if current.left == None:
                        current.left = new_node
                        return self
                    else:
                        current = current.left
    def __str__(self):
        return f"BST-> {self.root}"


# node = Node(10)
bst1 = BinarySearchTree()
bst1.insert(10)
bst1.insert(7)
bst1.insert(9)
bst1.insert(6)
bst1.insert(15)

print(bst1)