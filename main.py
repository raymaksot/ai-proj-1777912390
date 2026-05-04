from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        try:
            if self.root is None:
                self.root = Node(key)
            else:
                self._insert_recursive(self.root, key)
        except TypeError:
            raise ValueError("Key must be comparable to other keys")
        except RecursionError:
            raise RuntimeError("Tree depth exceeded recursion limit; consider balancing the tree")

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        # if key == node.key, do nothing (or handle duplicates)

    def search(self, key):
        try:
            return self._search_recursive(self.root, key)
        except TypeError:
            raise ValueError("Key must be comparable to other keys")
        except RecursionError:
            raise RuntimeError("Tree depth exceeded recursion limit during search")

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder(self):
        result = []
        try:
            self._inorder_recursive(self.root, result)
        except RecursionError:
            raise RuntimeError("Tree depth exceeded recursion limit during traversal")
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        result = []
        try:
            self._preorder_recursive(self.root, result)
        except RecursionError:
            raise RuntimeError("Tree depth exceeded recursion limit during traversal")
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        result = []
        try:
            self._postorder_recursive(self.root, result)
        except RecursionError:
            raise RuntimeError("Tree depth exceeded recursion limit during traversal")
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)

    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

def main():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Inorder traversal:", bst.inorder())
    print("Preorder traversal:", bst.preorder())
    print("Postorder traversal:", bst.postorder())
    print("Level-order traversal:", bst.level_order())

    print("Search 40:", bst.search(40))
    print("Search 123:", bst.search(123))

if __name__ == "__main__":
    main()