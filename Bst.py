#Task-4 Binary Search Tree (BST)
#Task: Use AI to create a BST with insert and in-order traversal methods.
#Sample Input Code:class BST:pass
#Expected Output:BST implementation with recursive insert and traversal methods.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
tree = BST()
root = None

root = tree.insert(root, 50)
tree.insert(root, 30)
tree.insert(root, 70)
tree.insert(root, 20)
tree.insert(root, 40)

tree.inorder(root)