DEFAULT_VALUES=[5,4,0,8,2,7]

class Node:
    
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return str(self.val) + " "

class BinaryTree:
    
    def __init__(self):
        self.root = None
        

    def getRoot(self):
        return self.root

    # Fill up the tree with recursively going through the nodes
    # It is not a balanced tree

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        elif val > node.val:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)


    def fillTree(self):
        useCustom = input("Want to add custom values?(y/n): ")
        if useCustom == "y":
            while True:
                userInput = input("Add value or quit with q: ")
                if userInput == "q":
                    break
                else:
                    try:
                        value = int(userInput)
                        self.add(value)
                    except:
                        print("Add integer numbers as values.")
        else:
            print("Adding default values.")
            for value in DEFAULT_VALUES:
                self.add(value)


    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)


    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node)
            self._printTree(node.right)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.fillTree()
    tree.printTree()