# week17-6.py 學習計畫 Heap / Priority Queue 第4題
# LeetCode 2462. Total Cost to Hire K Workers
# costs[i] 可聘第 i 個人。每次從「最左 or 最右」candidates 的數量裡，挑「最便宜」的人，共挑 k 人
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)  # 有 N 個工人
        if candidates * 2 + k > N:  # 狀況1: 最後一定全部都能挑，那就找最小的 K 個人
            heapify(costs)
            ans = 0
            for i in range(k):
                ans += heappop(costs)  # 要挑出 k 個工人
            return ans
        # 狀況2: 兩頭不會合作在一起，那我們就準備 2 堆 heap
        heap1, heap2 = [], []  # 把 heap 都長大成 k 個
        for i in range(candidates):
            heappush(heap1, costs[i])  # 左邊的候選人
            heappush(heap2, costs[N-1-i])  # 右邊的候選人
        ans = 0
        left, right = candidates, N-candidates-1
        for i in range(k):  # 要挑出 k 個工人
            if heap1[0] <= heap2[0]:  # 兩邊最小的，決定挑左邊的
                ans += heappop(heap1)  # 挑左邊的
                heappush(heap1, costs[left])
                left += 1
            else:
                ans += heappop(heap2)
                heappush(heap2, costs[right])
                right -= 1
        return ans