# week17-2.py 學習計畫 Trie 第2題
# LeetCode 1268. Search Suggestions System
# searchWord 每次輸入1個字母，找到對應的 products 前3名
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # 把所有的產品名字，照字母順序排序，以便插入時，字母小的在前面
        root = defaultdict(list)  # trie 的資料結構的1個node，當樹根
        for product in products:  # 很多產品 products 逐一張出1個產品 product
            now = root  # 每個產品，都要逐字母，在 trie 裡走下去
            for c in product:  # 逐字母加入 Trie（逐滑鼠建資料結構）
                if c not in now:
                    now[c] = defaultdict(list)  # 讓 node 就緒
                now = now[c]  # 再往下滑
            now['*'] = product  # 結尾打個「星星」產品名 直接放在裡面
        now = root  # 現在要開始一列一列，把 root 往下滑
        ans = []  # 把最接近的前3個 product 產品，塞到 ans 裡
        for c in searchWord:  # 逐個字母，每個字母輸入後，要找到 prefix 要找前3筆 best
            best = []  # 最好的前3筆產品 等一下要第一堆程式在這裡，找最好的前3筆...
            if c not in now:  # 根本就沒有延伸字母的 node，後面都沒有答案了
                noResult = len(searchWord) - len(ans)
                return ans + [[] for i in range(noResult)]  # 還欠幾筆答案
            now = now[c]  # 往下滑
            def helper(now):
                if '*' in now:
                    best.append(now['*'])  # 先查答案
                for c in now:
                    if len(best) < 3 and c != '*':
                        helper(now[c])
            helper(now)
            ans.append(best)
        return ans