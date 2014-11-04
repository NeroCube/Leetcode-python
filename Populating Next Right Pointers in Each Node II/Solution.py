# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
   		parent = root
   		while parent:
   			first = None
   			now = None
   			while parent:
   				if parent.left:
   					if first is None:
   						first = parent.left
   					else:
   						now.next = parent.left
   					now = parent.left
   				if parent.right:
   					if first is None:
   						first = parent.right
   					else:
   						now.next = parent.right
   					now = parent.right
   				parent = parent.next
   			parent = first

