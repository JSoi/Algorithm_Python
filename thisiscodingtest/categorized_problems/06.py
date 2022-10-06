# 무지의 먹방 라이브
# https://school.programmers.co.kr/learn/courses/30/lessons/42891
import collections
from heapq import heapify


def solution(food_times, k):
    count = 0
    idx = 0
    heap = []
    for i in range(len(food_times)):
        heap.heappush((food_times[i], i + 1))
    while count < k:
        # print(food_times[idx % len(food_times)])
        while food_times[idx % len(food_times)] <= 0:
            if idx >= 2 * len(food_times):
                return -1
            idx += 1
        food_times[idx % len(food_times)] -= 1
        idx = (idx + 1) % len(food_times)
        count += 1
    return idx % len(food_times) + 1


print(solution([3, 1, 2], 5))
