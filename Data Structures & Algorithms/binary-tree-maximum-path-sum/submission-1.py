# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -math.inf
        
        def dfs(node):
            nonlocal maxSum

            if not node: 
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            leftMax = max(leftSum, 0)
            rightMax = max(rightSum, 0)

            maxSum = max(maxSum, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        
        dfs(root)

        return maxSum
            