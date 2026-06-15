class Node:
    def __init__self(self,data):
        self.data=data
        self.left=None
        self.right=None

    def BST(root,minimum,maximum):
        if root is None:
            return True
        if root.data<=minimum or root.data>=maximum:
            return False
        return (BST(root.left,minimum,root.data)and BST(root.right,root.data,maximum))
root=Node(10)
root.left=Node(5)
root.right=Node(20)
if BST(root,float('-inf'),float('-inf')):
    print("BST")
else:
    print("Not BST")
