import pytest
from main import BinarySearchTree

def test_empty_tree():
    bst = BinarySearchTree()
    assert bst.inorder() == []
    assert bst.preorder() == []
    assert bst.postorder() == []
    assert bst.level_order() == []
    assert bst.search(10) == False

def test_single_node():
    bst = BinarySearchTree()
    bst.insert(42)
    assert bst.inorder() == [42]
    assert bst.search(42) == True
    assert bst.search(24) == False

def test_insert_and_search():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert bst.search(5) == True
    assert bst.search(15) == True
    assert bst.search(20) == False

def test_duplicate_insert():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    assert bst.inorder() == [10]
    assert bst.search(10) == True

def test_traversals():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)
    assert bst.inorder() == [20, 30, 40, 50, 60, 70, 80]
    assert bst.preorder() == [50, 30, 20, 40, 70, 60, 80]
    assert bst.postorder() == [20, 40, 30, 60, 80, 70, 50]
    assert bst.level_order() == [50, 30, 70, 20, 40, 60, 80]

def test_invalid_key_type():
    bst = BinarySearchTree()
    bst.insert(1)
    with pytest.raises(ValueError, match="Key must be comparable"):
        bst.insert("string")