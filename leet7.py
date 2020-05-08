# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if(root == None):
            return False
        x_info = []
        y_info = []
        d = 0
        parent = None
        
        self.depthfirst(root,x,y,0,None,x_info,y_info)
        return(x_info[0][0]==y_info[0][0] and x_info[0][1]!=y_info[0][1])
    
    def depthfirst(self,root,x,y,d,parent,x_info,y_info):
        if(root == None):
            return None
        if(root.val == x):
            x_info.append((d,parent))
        if(root.val == y):
            y_info.append((d,parent))
            
        self.depthfirst(root.left,x,y,d+1,root,x_info,y_info)
        self.depthfirst(root.right,x,y,d+1,root,x_info,y_info)
    
        