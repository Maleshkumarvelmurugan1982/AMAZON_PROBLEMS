class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(2)
root.left.right=Node(8)
key=int(input("Enter key to search:"))
current=root
while current is not None:
    if key==current.data:
        print("Found")
        break
    elif key<current.data:
        current=current.left
    else:
        current=current.right
if current is None:
    print("not Found")
