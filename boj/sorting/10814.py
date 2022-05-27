import collections
import heapq
import sys

cnt = int(sys.stdin.readline().strip())
dict = collections.defaultdict(list)
for _ in range(cnt):
    line = sys.stdin.readline().strip()
    age = int(line.split()[0])
    name = line.split()[1]
    dict[age].append(name)
heap = list()
for v in dict.keys():
    heapq.heappush(heap, v)
res = ''
for _ in range(len(heap)):
    d =heapq.heappop(heap)
    for ele in dict[d]:
        res += str(d) + ' ' + ele + '\n'
print(res)
