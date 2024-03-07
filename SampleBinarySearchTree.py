# The Node class with a default constructor
class Node:
    def __init__(self, key):
        self.key = key      # parameter to hold the value
        self.left = None    # parameter to hold the left sub-tree
        self.right = None   # parameter to hold the right sub-tree

# Implementation of BinarySearchTree class    
class BinarySearchTree:
    def __init__(self):
        self.root = None    # parameter to hold the root node
    
    # The insert() function to add a new Node to the BST
    def insert(self, key):
        self.root = self.insertNode(self.root, key)
        
    # A helper function to add a new node recursively
    def insertNode(self, root, key):
        # If the root is None (empty Node), return a new node
        if root is None:
            return Node(key)
        # If the key is smaller that root value, call insertNode() to add Node in left subtree
        if key < root.key:
            root.left = self.insertNode(root.left, key)      
        # otherwise, call insertNode() to add Node in right subtree
        else: 
            root.right = self.insertNode(root.right, key)
        return root
      
    # The inOrderTraversal function to do in-order tree traversal 
    def inOrderTraversal(self):
        output = []
        self.traverseBST(self.root, output)
        return output

    # A helper function to traverse tree recursively
    def traverseBST(self, root, output):   
        if root: 
            self.traverseBST(root.left, output) 
            output.append(root.key) 
            self.traverseBST(root.right, output) 
        return

# The treeSort function to perform sorting
def treeSort(arr): 
    bst = BinarySearchTree()
    # Adding elements to the binary search tree
    for element in arr:
        bst.insert(element)
    # returning the in-order traversal of the binary search tree
    return bst.inOrderTraversal()

if __name__ == '__main__':
    arr = [14, 13, 18, 11, 19, 12, 15, 16]
    print("Unsorted array:", arr)

    arr = treeSort(arr)
    print("Sorted array:", arr)