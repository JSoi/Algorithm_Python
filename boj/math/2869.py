import math
import sys

a, b, v = list(map(int, sys.stdin.readline().rstrip().split()))
# a 올라감, b 미끄러짐, 높이 v
movement = a - b
height = v - b
print(math.ceil(height / movement)) # 올림해서 가져와야 됩니다
