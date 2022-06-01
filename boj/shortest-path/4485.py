import heapq
import sys

ds = [0, 0, -1, 1]
dg = [-1, 1, 0, 0]
INF = int(1e09)
answer = ''
answercnt = 0
while True:
    cnt = int(sys.stdin.readline().rstrip())
    if cnt == 0:
        break
    block = []
    dist = [[INF] * cnt for _ in range(cnt)]
    for _ in range(cnt):
        block.append(list(map(int, sys.stdin.readline().rstrip().split())))

    q = [(block[0][0], 0, 0)]  # weight, s,g
    while q:
        w, ps, pg = heapq.heappop(q)
        if w > dist[ps][pg]:
            continue
        for k in range(4):
            ns, ng = ps + ds[k], pg + dg[k]
            if 0 <= ns < cnt and 0 <= ng < cnt:
                count = w + block[ns][ng]
                if count < dist[ns][ng]:
                    dist[ns][ng] = count
                    heapq.heappush(q, (count, ns, ng))
    answercnt += 1
    answer += 'Problem ' + str(answercnt) + ': ' + str(dist[cnt - 1][cnt - 1]) + '\n'
print(answer)