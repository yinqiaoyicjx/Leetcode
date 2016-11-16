
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]

        if root.left != None:
            result.append(self.inorderTraversal(root.left))
        result.append(root.val)
        if root.right != None:
            result.append(self.inorderTraversal(root.right))
        return result

