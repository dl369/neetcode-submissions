# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        def checkTree(root, subRoot):
            if not root:
                return not subRoot
            if not subRoot:
                return False
            
            if root.val == subRoot.val:
                return checkTree(root.left, subRoot.left) and checkTree(root.right, subRoot.right)
            else:
                return False
        
        def dfs(root):
            if not root:
                return False
            
            if root.val == subRoot.val:
                if checkTree(root, subRoot):
                    return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)