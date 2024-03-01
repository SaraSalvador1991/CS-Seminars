from classes.node_bin_tree import Node
from typing import List, Tuple
from graphviz import Digraph


class BinaryTree(object):
    # class variables
    count_trees = 0

    def __init__(self):
        # instance variables
        self.root = None
        self.size = 0
        BinaryTree.count_trees += 1

    def __del__(self):
        BinaryTree.count_trees -= 1

    def insert(self, key: int) -> None:
        node = Node(key)
        if self.size == 0:
            self.root = node  # create the root of the tree
        else:
            self._insert_rec(node, self.root)  # if root exists, insert key recursive
        self.size += 1

    def _insert_rec(self, insert_node: Node, current_node: Node) -> None:
        if insert_node.get_key() < current_node.get_key():
            if current_node.get_left() is None:
                current_node.set_left(insert_node)
            else:
                self._insert_rec(insert_node, current_node.get_left())
        elif insert_node.get_key() > current_node.get_key():
            if current_node.get_right() is None:
                current_node.set_right(insert_node)
            else:
                self._insert_rec(insert_node, current_node.get_right())
        else:
            raise ValueError("Key already exists in the binary tree.")

    def find(self, key: int) -> bool:
        return self._find_rec(key, self.root)

    def _find_rec(self, key: int, current_node: Node) -> bool:
        if current_node is None:
            return False
        elif key == current_node.get_key():
            return True
        elif key < current_node.get_key():
            return self._find_rec(key, current_node.get_left())
        else:  # key > current_node.get_key()
            return self._find_rec(key, current_node.get_right())

    def delete(self, key: int) -> None:
        if not self._delete_rec(key, self.root, self.root):
            raise ValueError("Key does not exist in the binary tree.")
        self.size -= 1

    def _delete_rec(self, key: int, current_node: Node, previous_node: Node) -> bool:
        if current_node is None:
            return False
        elif key < current_node.get_key():
            return self._delete_rec(key, current_node.get_left(), current_node)
        elif key > current_node.get_key():
            return self._delete_rec(key, current_node.get_right(), current_node)
        else:  # key == current_node.get_key()
            if current_node.get_left() is None and current_node.get_right() is None:
                if current_node.get_key() < previous_node.get_key():
                    previous_node.set_left(None)
                else:  # current_node.get_key() > previous_node.get_key()
                    previous_node.set_right(None)
            elif current_node.get_left() is not None and current_node.get_right() is None:
                if current_node.get_key() < previous_node.get_key():
                    previous_node.set_left(current_node.get_left())
                else:  # current_node.get_key() > previous_node.get_key()
                    previous_node.set_right(current_node.get_left())
            elif current_node.get_right() is not None and current_node.get_left() is None:
                if current_node.get_key() < previous_node.get_key():
                    previous_node.set_left(current_node.get_right())
                else:  # current_node.get_key() > previous_node.get_key()
                    current_node.set_right(current_node.get_right())
            else:  # current_node.get_left() is not None and current_node.get_right() is not None
                # Find the largest key in left subtree of the node to be deleted and move that key up.
                if current_node.get_left().get_right() is not None:
                    lakelesu = self._find_lakelesu_rec(current_node.get_left(), current_node)
                else:
                    lakelesu = current_node.get_left().get_key()
                    if current_node.get_left().get_left() is not None:
                        current_node.set_left(current_node.get_left().get_left())
                    else:
                        current_node.set_left(None)
                current_node.set_key(lakelesu)
            return True

    def _find_lakelesu_rec(self, current_node: Node, previous_node: Node) -> int:
        if current_node.get_right() is not None:
            return self._find_lakelesu_rec(current_node.get_right(), current_node)
        if current_node.get_left() is None:
            previous_node.set_right(None)
        else:
            previous_node.set_right(current_node.get_left())
        return current_node.get_key()

    def print_tree(self) -> None:
        if self.root is not None:
            tree = Digraph()
            preorder_list, tree = self._print_tree_rec(self.root, list(), tree)
            print(f"Preorder: {preorder_list}")
            tree.render(filename='binary_tree', view=True, format='png')
        else:
            print("The tree is empty.")

    def _print_tree_rec(self, current_node: Node, pre_list: List, tree: Digraph) -> Tuple[List, Digraph]:
        pre_list.append(current_node.get_key())
        tree.node(str(current_node.get_key()), str(current_node.get_key()))
        if current_node.get_left() is not None:
            tree.edge(str(current_node.get_key()), str(current_node.get_left().get_key()))
            pre_list, tree = self._print_tree_rec(current_node.get_left(), pre_list, tree)
        if current_node.get_right() is not None:
            tree.edge(str(current_node.get_key()), str(current_node.get_right().get_key()))
            pre_list, tree = self._print_tree_rec(current_node.get_right(), pre_list, tree)
        return pre_list, tree

    def get_size(self) -> int:
        return self.size

    def get_height(self) -> int:
        return self._get_height_rec(self.root)

    def _get_height_rec(self, node: Node) -> int:
        if node is None:
            return -1
        height_left = self._get_height_rec(node.get_left())
        height_right = self._get_height_rec(node.get_right())
        return max(height_left, height_right) + 1

    def burn_off(self) -> None:
        self.root = None
        self.size = 0
