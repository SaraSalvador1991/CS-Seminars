from classes.node_bin_tree import Node
from typing import List, Tuple
from graphviz import Digraph
from queue import Queue


class BinaryTree(object):
    """
    Represents a binary tree data structure.

    Class Variables:
        - count_trees (int): The number of BinaryTree instances created.

    Attributes:
        - root (Node): The root node of the binary tree.
        - size (int): The number of keys in the tree.

    Methods:
        - __init__(): Initializes a BinaryTree instance.
        - __del__(): Deletes a BinaryTree instance.
        - insert(key: int) -> None: Inserts a key into the tree.
        - _insert_rec(insert_node: Node, current_node: Node) -> None: Inserts a node recursively into the binary tree.
        - find(key: int) -> bool: Finds if the key exists in the binary tree.
        - _find_rec(key: int, current_node: Node) -> bool: Finds a key recursively in the binary tree.
        - delete(key: int) -> None: Deletes a node with the given key from the binary tree.
        - _delete_rec(key: int, current_node: Node, previous_node: Node) -> bool: Deletes a node recursively from the
          * binary tree.
        - _find_lakelesu_rec(current_node: Node, previous_node: Node) -> int: Recursively finds the rightmost node in
          * the tree.

    """
    # class variables
    count_trees = 0

    def __init__(self):
        # instance variables
        self.root = None
        self.size = 0  # number of keys in the tree
        BinaryTree.count_trees += 1

    def __del__(self):
        """
        Deletes an instance of the BinaryTree class.

        :return: None
        """
        BinaryTree.count_trees -= 1

    def insert(self, key: int) -> None:
        """
        Insert a key into the tree.

        :param key: The key to be inserted into the tree.
        :return: None
        """
        node = Node(key)
        if self.size == 0:
            self.root = node  # create the root of the tree
        else:
            self._insert_rec(node, self.root)  # if root exists, insert key recursive
        self.size += 1

    def _insert_rec(self, insert_node: Node, current_node: Node) -> None:
        """
        Insert a node recursively into the binary tree.

        :param insert_node: The node to insert.
        :param current_node: The current node in the recursion.
        :return: None
        :raises ValueError: If the key already exists in the binary tree.
        """
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
        """
        Finds if the key exists in the data structure.

        :param key: The key to search for.
        :return: True if the key is found, False otherwise.
        """
        return self._find_rec(key, self.root)

    def _find_rec(self, key: int, current_node: Node) -> bool:
        """
        Find a key recursively in a binary search tree.

        :param key: The key to search for.
        :param current_node: The current node being evaluated.
        :return: True if the key is found, False otherwise.
        """
        if current_node is None:
            return False
        elif key == current_node.get_key():
            return True
        elif key < current_node.get_key():
            return self._find_rec(key, current_node.get_left())
        else:  # key > current_node.get_key()
            return self._find_rec(key, current_node.get_right())

    def delete(self, key: int) -> None:
        """
        Deletes a node with the given key from the binary tree.

        :param key: The key of the node to be deleted.
        :return: None
        :raises ValueError: If the key does not exist in the binary tree.
        """
        if not self._delete_rec(key, self.root, self.root):
            raise ValueError("Key does not exist in the binary tree.")
        self.size -= 1

    def _delete_rec(self, key: int, current_node: Node, previous_node: Node) -> bool:
        """
        This method is a recursive helper function for deleting a node with a given key from a binary search tree.
        It recursively searches for the node with the given key and deletes it from the tree.
        If the node is found and deleted, the method returns True. Otherwise, it returns False.

        The method follows the following logic:
        1. Check if the current node is None. If so, return False as the key was not found in the tree.
        2. Check if the key is less than the current node's key. If so, recursively call the method with the left child
           * of the current node as the new current node and the current node as the new previous node.
        3. Check if the key is greater than the current node's key. If so, recursively call the method with the right
           * child of the current node as the new current node and the current node as the new previous node.
        4. If none of the above conditions are met, it means that the key is equal to the current node's key. Perform
           * the following deletion logic:
           - If the current node has no children, update the appropriate child of the previous node to None, depending
             * on whether the current node is the left or right child. Or if the current node is the root, set the root
             * to None.
           - If the current node has only a left child, update the appropriate child of the previous node to the left
             * child. Or if the current node is the root, set the left child of the root as the new root.
           - If the current node has only a right child, update the appropriate child of the previous node to the right
             * child. Or if the current node is the root, set the right child of the root as the new root.
           - If the current node has both a left and right child, find the largest key in the left subtree of the
             * current node (called "lakelesu") and replace the current node's key with lakelesu. If the left child of
             * the current node does not have a right child, the lakelesu is already found. Otherwise, find recursively
             * the rightmost node of the left subtree.
        5. After performing the deletion, return True.

        Note: This method should only be called as a helper function within the context of a binary search tree class.

        :param key: The key of the node to be deleted.
        :param current_node: The current node being checked.
        :param previous_node: The previous node of the current node (parent node).
        :return: True if the node is successfully deleted, False otherwise.
        """
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
                elif current_node.get_key() > previous_node.get_key():
                    previous_node.set_right(None)
                else:  # current_node == previous_node -> we are at the root.
                    self.root = None
            elif current_node.get_left() is not None and current_node.get_right() is None:
                if current_node.get_key() < previous_node.get_key():
                    previous_node.set_left(current_node.get_left())
                elif current_node.get_key() > previous_node.get_key():
                    previous_node.set_right(current_node.get_left())
                else:  # current_node == previous_node -> we are at the root.
                    self.root = current_node.get_left()
            elif current_node.get_right() is not None and current_node.get_left() is None:
                if current_node.get_key() < previous_node.get_key():
                    previous_node.set_left(current_node.get_right())
                elif current_node.get_key() > previous_node.get_key():
                    current_node.set_right(current_node.get_right())
                else:  # current_node == previous_node -> we are at the root.
                    self.root = current_node.get_right()
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
        """
        Recursively finds the rightmost node in the tree rooted at `current_node`, performing some modification on the
        * tree structure along the way.

        If the current node has a right child, the method continues recursively with the right child as the new
        * `current_node` and the current node as the new `previous_node`.

        If the node with the lakelesu (current node) was found, the method follows the following logic:
        1. If the current node does not have a left child, the right child of the previous node is set to None.
        2. If the current node has a left child, the right child of the previous node is set to the left child.
        3. Finally, the key of the current node that has been processed is returned.

        :param current_node: The current node being processed.
        :param previous_node: The previous node in the tree.
        :return: The key of the current node that has been processed.
        """
        # If the right child of the current_node is not None, go deeper.
        if current_node.get_right() is not None:
            return self._find_lakelesu_rec(current_node.get_right(), current_node)
        # If the rightmost node (lakelesu) was reached, set the right child of the previous node accordingly.
        if current_node.get_left() is None:
            previous_node.set_right(None)
        else:
            previous_node.set_right(current_node.get_left())
        return current_node.get_key()

    def print_tree_dfs(self) -> None:
        """
        Print the nodes of the binary tree using depth-first search (DFS) and visualize the tree.

        :return: None
        """
        if self.root is not None:
            tree = Digraph()
            preorder_list, inorder_list, postorder_list, tree = self._print_tree_dfs_rec(self.root, list(), list(), list(), tree)
            print(f"Pre-order: {preorder_list}")
            print(f"In-order: {inorder_list}")
            print(f"Post-order: {postorder_list}")
            tree.render(filename='binary_tree', view=True, format='png')
        else:
            print("The tree is empty.")

    def _print_tree_dfs_rec(self, current_node: Node, pre_list: List, in_list: List, post_list: List, tree: Digraph) -> Tuple[List, List, List, Digraph]:
        """
        This method performs a recursive depth-first search traversal of the tree starting from the given current node.
        It updates the pre_list, in_list, and post_list by appending the keys of the visited nodes in the respective
        * traversal order.
        It also updates the tree by adding nodes and edges corresponding to the visited nodes (in pre-order manner).

        :param current_node: The current node being traversed in the tree.
        :param pre_list: A list to store the keys of the nodes visited in pre-order traversal.
        :param in_list: A list to store the keys of the nodes visited in in-order traversal.
        :param post_list: A list to store the keys of the nodes visited in post-order traversal.
        :param tree: A Digraph object representing the tree.
        :return: A tuple containing the updated lists (pre_list, in_list, post_list) and the Digraph object (tree).
        """
        # Append the key of the current_node to the pre-order list BEFORE visiting the left and right child.
        pre_list.append(current_node.get_key())
        tree.node(str(current_node.get_key()), str(current_node.get_key()))
        if current_node.get_left() is not None:
            tree.edge(str(current_node.get_key()), str(current_node.get_left().get_key()))
            pre_list, in_list, post_list, tree = self._print_tree_dfs_rec(current_node.get_left(), pre_list, in_list, post_list, tree)
        # Append the key of the current_node to the in-order list AFTER visiting the left child but BEFORE visiting the
        # * right child.
        in_list.append(current_node.get_key())
        if current_node.get_right() is not None:
            tree.edge(str(current_node.get_key()), str(current_node.get_right().get_key()))
            pre_list, in_list, post_list, tree = self._print_tree_dfs_rec(current_node.get_right(), pre_list, in_list, post_list, tree)
        # Append the key of the current_node to the post-order list AFTER visiting the left and right child.
        post_list.append(current_node.get_key())
        return pre_list, in_list, post_list, tree

    def print_tree_bfs(self) -> None:
        """
        Prints the tree using breadth-first search (BFS) traversal with a queue data structure.

        :return: None
        """
        if self.root is not None:
            bfs_list = [self.root.get_key()]
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                # Get the next node in the queue.
                current_node = queue.get()
                # If the left child is not None enqueue it and append its key to the bfs list.
                if current_node.get_left() is not None:
                    bfs_list.append(current_node.get_left().get_key())
                    queue.put(current_node.get_left())
                # If the right child is not None enqueue it and append its key to the bfs list.
                if current_node.get_right() is not None:
                    bfs_list.append(current_node.get_right().get_key())
                    queue.put(current_node.get_right())
            print(f"Breadth-first: {bfs_list}")
        else:
            print("The tree is empty.")

    def get_size(self) -> int:
        """
        Get the size of the object (number of nodes in the binary tree).

        :return: The size of the object.
        """
        return self.size

    def get_height(self) -> int:
        """
        Get the height of the binary tree.
        The height of an empty binary tree is 0.
        The height of a binary tree with a single node (root) is 1.

        :return: The height of the binary tree.
        """
        return self._get_height_rec(self.root)

    def _get_height_rec(self, node: Node) -> int:
        """
        Recursively calculates the height of a binary tree starting from the given node.

        :param node: The root node of the current subtree.
        :return: The height of the binary tree.
        """
        if node is None:
            return 0
        height_left = self._get_height_rec(node.get_left())
        height_right = self._get_height_rec(node.get_right())
        return max(height_left, height_right) + 1

    def burn_off(self) -> None:
        """
        Clears the binary tree by setting the root to None.

        :return: None
        """
        self.root = None
        self.size = 0
