# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        index = {}
        start = answer = 0
        for i, c in enumerate(s):
            if c in index and start<=index[c]:
                start = index[c]+1
            else: # 중복 없을시
                answer = max(answer, i-start+1)
            index[c] = i
        return answer

    def lengthOfLongestSubstring_slow(self, s: str) -> int:  # mysolution..but slow
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        answer = ""
        while l < r and r <= len(s):
            now = s[l:r]
            if len(set(list(now))) != len(now):  # 중복된경우
                l += 1
                r = l + 1
            else:  # 중복되지 않은 경우
                answer = max(answer, s[l:r], key=len)
                r += 1
        print(answer)
        return len(answer)
