import sys

a, b = map(int, input().split())
my_map = {}
for _ in range(a):
    site, password = sys.stdin.readline().split()
    my_map[site] = password
answer = ""
for _ in range(b):
    target = sys.stdin.readline().strip()
    answer += my_map[target] + "\n"
print(answer)
