class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False

        return True