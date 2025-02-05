import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_post_order(node):
    if node is None:
        return 0, 0  # (bilancio monete, numero di mosse)

    left_balance, left_moves = dfs_post_order(node.left)
    right_balance, right_moves = dfs_post_order(node.right)
    total_moves = abs(left_balance) + abs(right_balance)

    return node.val - 1 + left_balance + right_balance, left_moves + right_moves + total_moves

class TestDistributeCoins(unittest.TestCase):
    def test_case_1(self):
        root = TreeNode(3)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertEqual(dfs_post_order(root)[1], 2) 

if __name__ == '__main__':
    unittest.main()

# The DFS Post-Order algorithm is used to redistribute coins in a binary tree with the minimum number of moves.
# Processes left child, then right child, then current node.
# Time Complexity and Space Complixty equal to O(n) and O(h), the latter, Depends on tree height (logarithmic for balanced trees, linear for skewed trees).