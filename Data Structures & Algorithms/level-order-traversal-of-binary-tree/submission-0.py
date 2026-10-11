# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        p=deque([root])
        newlist=[]
        while p:
            listtoadd=[]
            for i in range(len(p)):
                node=p.popleft()
                if node:
                    listtoadd.append(node.val)
                    p.append(node.left)
                    p.append(node.right)
            if listtoadd:
                newlist.append(listtoadd)
        return newlist
    