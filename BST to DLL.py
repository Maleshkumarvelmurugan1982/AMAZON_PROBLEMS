class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


prev = None
head = None


def convert(root):
    global prev, head

    if root is None:
        return

    convert(root.left)

    if prev is None:
        head = root
    else:
        prev.right = root
        root.left = prev

    prev = root

    convert(root.right)


# Tree
root = Node(1)
root.left = Node(3)
root.right = Node(2)

convert(root)

current = head

while current:
    print(current.data, end=" <-> ")
    current = current.right

print("None")
