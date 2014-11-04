# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
    	ret = []
    	if root is None:
    		return ret
    	ret.extend( self.inorderTraversal(root.left) )
    	ret.append( root.val )
    	ret.extend( self.inorderTraversal(root.right) )
        return ret

    #No recursion
    def inorderTraversal1(self, root):
    	ret, stack, now = [], [], root
    	while stack or now:
    		if now:
    			stack.append(now)
    			now = now.left
    		else:
    			p = stack.pop()
    			ret.append( p.val )
    			now = p.right

    	return ret
  
if __name__ == '__main__':
	root = TreeNode(1)
	left = TreeNode(2)
	root.left = left
	print Solution().inorderTraversal1(root)