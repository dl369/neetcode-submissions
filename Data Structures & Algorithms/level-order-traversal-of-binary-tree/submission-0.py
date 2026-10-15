# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 1))

        res = []
        
        currList = []
        currDepth = 1

        while q:
            (node, depth) = q.popleft()

            if depth > currDepth:
                res.append(currList)
                currList = []
                currDepth += 1

            if node:
                currList.append(node.val)
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
        
        return res