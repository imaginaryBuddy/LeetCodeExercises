# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        temp = []
        level = 0
        currLevel = level 
        pq = queue.Queue() 

        pq.put([level, root])

        while(not pq.empty()):
            node = pq.get() 
            if node[0] != currLevel:
                res.append(temp)
                temp = [] 
                currLevel = node[0]
            # explore left and right 
            if node[1]: 
                temp.append(node[1].val)
                pq.put([node[0]+1, node[1].left])
                pq.put([node[0]+1, node[1].right])

        return res
