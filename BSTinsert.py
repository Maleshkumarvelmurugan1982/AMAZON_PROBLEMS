class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(8)

value = int(input("Enter value to insert: "))

current = root

while True:

    if value < current.data:

        if current.left is None:
            current.left = Node(value)
            print("Inserted")
            break

        current = current.left

    elif value > current.data:

        if current.right is None:
            current.right = Node(value)
            print("Inserted")
            break

        current = current.right

    else:
        print("Value already exists")
        break
