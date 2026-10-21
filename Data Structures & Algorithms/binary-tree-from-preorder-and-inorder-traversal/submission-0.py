# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodeMap = {}
        for i, val in enumerate(inorder):
            nodeMap[val] = i
        
        preOrderIdx = 0

        size = len(preorder)

        def build(l, r):
            nonlocal preOrderIdx
            
            if r < 0 or l > size - 1 or r < l:
                return

            currRootVal = preorder[preOrderIdx]
            inOrderIdx = nodeMap[currRootVal]

            node = TreeNode(currRootVal)
            preOrderIdx += 1

            node.left = build(l, inOrderIdx - 1)
            node.right = build(inOrderIdx + 1, r)

            return node
        
        return build(0, size)

