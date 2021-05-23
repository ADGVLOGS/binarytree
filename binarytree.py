#ADG 2021 INVERT BINARY TREE

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def InvertBinary(tree):
 if tree:
  left = tree.left
  right = tree.right
  tree.left = right
  tree.right = left 
  InvertBinary(tree.left)
  InvertBinary(tree.right)

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)


print("Binary Tree")
root.PrintTree()

print("Invert Binary Tree")
InvertBinary(root)
root.PrintTree()

