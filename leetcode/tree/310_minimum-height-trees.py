import collections
from typing import List


class Solution:
    def findMinHeightTrees_timeout(self, n: int, edges: List[List[int]]) -> List[int]:
        # 다 탐색해서 dictionary 에 집어넣자 ^^..
        def height(node, visit):
            minimax = 0
            for i in map[node]:
                if visit[i]:
                    continue
                visit[i] = True
                minimax = max(minimax, height(i, visit) + 1)
            return minimax

        map = collections.defaultdict(list)

        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])

        print(map)

        answer = collections.defaultdict(list)
        for i in range(n):
            visit = [False] * n
            visit[i] = True
            a = height(i, visit)
            answer[a].append(i)
        answer = sorted(answer.items())
        # print('abs' , answer)
        if not answer:
            return [0]
        return answer[0][1]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 다 탐색해서 dictionary 에 집어넣자 ^^..
        if n <= 1:
            return [0]

        map = collections.defaultdict(list)

        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])

        leaves = []
        for m in map:
            if len(map[m]) == 1:
                leaves.append(m)

        while n > 2:
            newleaves = []
            n -= len(leaves)
            for l in leaves:
                conn = map[l].pop()
                map[conn].remove(l)
                if len(map[conn]) == 1:
                    newleaves.append(conn)
            leaves = newleaves
        return leaves


# n = 6
# edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
n = 2
edges = [[0, 1]]
sol = Solution()
print(sol.findMinHeightTrees(n, edges))
