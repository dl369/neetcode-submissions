# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
            
        q = deque()
        q.append(root)
        res = []

        while q:
            node = q.pop()

            if not node:
                res.append("null")
            else:
                res.append(str(node.val))
                
                # Because it's a LIFO stack, push RIGHT first so LEFT is popped first.
                # This perfectly mirrors the Root -> Left -> Right recursion in deserialize.
                q.append(node.right)
                q.append(node.left)
        
        return " ".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split()
        length = len(data)
        
        def build(idx):
            if idx >= length:
                return (None, 0)
            
            val = data[idx]
            if val == "null":
                return (None, 1)

            node = TreeNode(val)
            idx += 1
            node.left, numChildrenLeft = build(idx)
            
            idx += numChildrenLeft
            node.right, numChildrenRight = build(idx)

            return node, 1 + numChildrenLeft + numChildrenRight
        
        return build(0)[0]
            