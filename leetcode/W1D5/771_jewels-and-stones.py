# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mydic = dict()
        for c in range(len(jewels)):
            mydic[jewels[c]] = 0
        for st in range(len(stones)):
            if mydic.get(stones[st]) is not None:
                mydic[stones[st]] = mydic.get(stones[st])+1
        answer = 0
        for val in mydic.values():
            answer += val
        return answer