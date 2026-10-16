# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, smallest, biggest):
            if not node.left and not node.right:
                return True

            if not node.right:
                if node.left.val < node.val and node.left.val > smallest:
                    return dfs(node.left, smallest, node.val)
                else:
                    return False
            elif not node.left:
                if node.right.val > node.val and node.right.val < biggest:
                    return dfs(node.right, node.val, biggest)
                else:
                    return False
            else:
                if node.left.val < node.val and node.right.val > node.val and node.left.val > smallest and node.right.val < biggest:
                    return dfs(node.left, smallest, node.val) and dfs(node.right, node.val, biggest)
                else:
                    return False

        return dfs(root, -math.inf, math.inf)