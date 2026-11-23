# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        idx = 0

        def solve(left, right):
            nonlocal idx

            if left > right:
                return None

            node = TreeNode(preorder[idx])
            target_idx = inorder.index(preorder[idx])
            idx += 1

            node.left = solve(left, target_idx - 1)
            node.right = solve(target_idx + 1, right) 
        
            return node

        return solve(0, len(inorder) - 1)
