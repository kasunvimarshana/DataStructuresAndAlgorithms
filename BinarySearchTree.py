import graphviz
import os

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.key:
                root.left = self._insert(root.left, key)
            else:
                root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._get_min_value(root.right)
            root.right = self._delete(root.right, root.key)
        return root

    def _get_min_value(self, root):
        while root.left is not None:
            root = root.left
        return root.key

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.key, end=' ')
            self._inorder_traversal(root.right)

    def generate_graphviz(self, filename):
        dot = graphviz.Digraph()
        dot.format = 'png'

        def add_node(root):
            if root:
                dot.node(str(root.key))
                if root.left:
                    dot.edge(str(root.key), str(root.left.key))
                    add_node(root.left)
                if root.right:
                    dot.edge(str(root.key), str(root.right.key))
                    add_node(root.right)

        add_node(self.root)
        dot.render(filename, view=True)


if __name__ == '__main__':
    # Example usage
    # os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

    print(os.environ["PATH"])

    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    bst.generate_graphviz("bst.png")