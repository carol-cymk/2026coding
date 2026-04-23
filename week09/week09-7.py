# week09-7.py Linked List 第4題
# LeetCode 2130. Maximum Twin Sum of a Linked List

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []

        # 1. 先把 linked list 轉成陣列
        while head:
            a.append(head.val)
            head = head.next

        # 2. 雙指標（頭尾配對）
        N = len(a)
        ans = 0

        for i in range(N // 2):  # 只需要跑一半！！
            ans = max(ans, a[i] + a[N - 1 - i])

        return ans