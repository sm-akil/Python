class N:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val),
        Inorder(root.right)


def Preorder(root):
    if root:
        print(root.val),
        Preorder(root.left)
        Preorder(root.right)


root = N(2)
root.left = N(4)
root.right = N(6)
root.left.left = N(8)
root.left.right = N(10)
print("Preorder traversal binary tree : ")
Preorder(root)

print("Inorder traversal binary tree : ")
Inorder(root)
