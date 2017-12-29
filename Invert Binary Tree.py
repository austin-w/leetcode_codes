# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        if root == None :
            return root
        if root.left == None and root.right == None :
            return root
        else :
            temp = root.left
            root.left = root.right
            root.right = temp 
            if root.left == None and root.right == None :
                return root
            else :
                self.invertTree(root.left)
                self.invertTree(root.right)
                
        return root     
                
