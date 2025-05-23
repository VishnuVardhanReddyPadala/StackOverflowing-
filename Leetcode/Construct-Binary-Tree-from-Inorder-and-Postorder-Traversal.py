class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index_in_inorder = inorder.index(root_val)

        root.right = self.buildTree(inorder[root_index_in_inorder + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index_in_inorder], postorder)

        return root