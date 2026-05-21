# week13-1.py 學習計畫 Graph - BFS 第1題
# LeetCode 1926. Nearest Exit from Entrance in Maze
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        
        visited = set()
        visited.add(tuple(entrance))
        
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))
        
        while queue:
            i, j, step = queue.popleft()
            
            for ii, jj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if ii < 0 or jj < 0 or ii >= M or jj >= N:
                    continue
                
                if maze[ii][jj] == '+':
                    continue
                
                if (ii, jj) not in visited:
                    if ii == 0 or jj == 0 or ii == M-1 or jj == N-1:
                        return step + 1
                    
                    visited.add((ii, jj))
                    queue.append((ii, jj, step + 1))
        
        return -1