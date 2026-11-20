# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        
        #     return max(left, right) + 1
        
        # return dfs(root)

        q = []
        if root:
            q.append(root)

        level = 0
        while q:
            for _ in range(len(q)):
                node = q[0]
                q = q[1:]

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return level


