# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

"""
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous
to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

         4
      2    5
    1  3


We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor.
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above.
The "head" symbol means the node it points to is the smallest element of the linked list.


head =    --> 1 <-> 2 <-> 3 <-> 4 <-> 5 <--
          ^-------------------------------^


Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor.
We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.



"""


# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            head, tail = node, node

            if node.left:
                left_head, left_tail = helper(node.left)
                left_tail.right = node
                node.left = left_tail
                head = left_head

            if node.right:
                right_head, right_tail = helper(node.right)
                right_head.left = node
                node.right = right_head
                tail = right_tail

            return head, tail

        if root:
            head, tail = helper(root)
            head.left = tail
            tail.right = head

            return head

        return root
