# https://leetcode.com/problems/group-anagrams/
# Group Anagram
import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    #print(anagrams)
    for s in strs:
        # sorted : 파이썬 리스트를 정렬해서 리스트로 반환 -> join 사용 필요
        anagrams[''.join(sorted(s))].append(s)
    # print(anagrams.values())
    return anagrams.values()


test = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(test)
