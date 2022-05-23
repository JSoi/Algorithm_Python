# https://leetcode.com/problems/top-k-frequent-elements/
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)  # collections.Counter 사용 시 Dictionary형으로 만들어준다
        answer = []
        for i in count.most_common(k):
            answer.append(i[0])
        return answer

    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)  # collections.Counter 사용 시 Dictionary형으로 만들어준다
        answer = []
        sorted_dict = sorted(count.items(), key=lambda item: item[1], reverse=True) # sort 하는 방식
        #count.items들을 람다식으로
        for mk in range(k):
            answer.append(sorted_dict[mk][0])
        return answer


sol = Solution()
sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
