class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.maxDepth = 0

        def dfs(node,left,right):
            self.maxDepth = max(self.maxDepth, left, right)

            if node.left:
                dfs(node.left, right+1, 0)

            if node.right:
                dfs(node.right, 0, left+1)
        
        dfs(root,0,0)
        return self.maxDepth