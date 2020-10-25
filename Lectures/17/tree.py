class BinaryTree:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert into BinaryTree
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the Tree Out
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res




if __name__ == "__main__":
    bt = BinaryTree(27)
    bt.insert(14)
    bt.insert(35)
    bt.insert(10)
    bt.insert(19)
    bt.insert(31)
    bt.insert(42)

    print(bt.inorderTraversal(bt))

