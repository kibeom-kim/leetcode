# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        answer = []

        if not root:
            return answer

        # q = list()
        q = collections.deque()
        q.append((root, 1))

        while q:
            # node, level = q[0]
            # q = q[1:]
            node, level = q.popleft()
            
            if len(answer) < level:
                answer.append([])

            answer[level - 1].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            
            if node.right:
                q.append((node.right, level + 1))

        return answer
