# week17-5.py 學習計畫 Binary Tree - BFS
# LeetCode 1161. Maximum Level Sum of a Binary Tree
# 想知道 tree 每一層加起來, 哪一層最大?
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = []  # 每一層加起來的結果,放這裡
        def helper(root, level):  # 在第 level 層的 root node
            if root == None: return  # 終止條件, 不要再處理了
            if level >= len(levelSum):
                levelSum.append(0)  # 多一層
            levelSum[level] += root.val  # 加起來
            helper(root.left, level + 1)  # 函式呼叫函式
            helper(root.right, level + 1)  # 函式呼叫函式
        helper(root, 0)  # 函式呼叫函式
        M = max(levelSum)  # 找到 levelSum 裡的最大值
        return levelSum.index(M) + 1  # 找到第1個最大值的 index, 改成 1-index