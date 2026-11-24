# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # 1
        # def dfs(node):
        #     if not node:
        #         return True, float("inf"), float("-inf")
            
        #     left_valid, left_min, left_max = dfs(node.left)
        #     right_valid, right_min, right_max = dfs(node.right)

        #     if not left_valid or not right_valid:
        #         return False, None, None

        #     if left_max >= node.val or right_min <= node.val:
        #         return False, None, None
            
        #     return True, min(left_min, node.val), max(right_max, node.val)


        # is_valid, _, _ = dfs(root)
        
        # return is_valid

        # 2
        def validate(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))
        
