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

            if leftSum <= 0:
                if rightSum <= 0:
                    maxSum = max(node.val, maxSum)
                    return node.val
                else:
                    maxSum = max(node.val + rightSum, maxSum)
                    return node.val + rightSum
            else:
                if rightSum <= 0:
                    maxSum = max(node.val + leftSum, maxSum)
                    return node.val + leftSum
                else:
                    maxSum = max(node.val + rightSum + leftSum, maxSum)
                    return max(rightSum, leftSum) + node.val
        
        dfs(root)

        return maxSum
            