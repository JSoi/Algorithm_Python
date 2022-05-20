import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 방향이 존재한다!
        mydict = collections.defaultdict(list)
        tickets = sorted(tickets, key=lambda x: x[1], reverse=True)
        print('tickets', tickets)
        for ti in tickets:
            mydict[ti[0]].append(ti[1])
        queue = collections.deque()
        queue.append('JFK')
        visit = list()
        while queue:
            popqueue = queue.pop()
            visit.append(popqueue)  # 정답에 붙여넣기
            while mydict[popqueue]:
                if queue and mydict[popqueue][0] > queue[0]:
                    queue.appendleft(mydict[popqueue].pop(0))
                else:
                    queue.append(mydict[popqueue].pop(0))
        print(visit)


myinput = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
sol = Solution()
print(sol.findItinerary(myinput))
