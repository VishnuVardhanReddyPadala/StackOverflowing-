# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: bool
        \\\
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
        
        return is_mirror(root, root)