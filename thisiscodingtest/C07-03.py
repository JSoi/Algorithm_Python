# p.201
import sys

cnt, length = map(int, sys.stdin.readline().split())
ddeok = list(map(int, sys.stdin.readline().split()))
print(ddeok)
longest_ddeok = max(ddeok)
start,end= 0,longest_ddeok-1
longest = 0
while start<end:
    mid = (start+end)//2
    cut = 0
    for d in ddeok:
        if d>mid:
            cut+=(d-mid)
    if cut==length:
        return
    longest += cut
print(longest)