# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]

        p=deque([root])

        while p:
            for i in range(len(p)):
                node=p.popleft();

                if node:
                    p.append(node.left)
                    p.append(node.right)
                    res.append(node.val)

        res.sort()

        return res[k-1]
                