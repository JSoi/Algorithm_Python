from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a1, a2):
            if int(str(a1) + str(a2)) >= int(str(a2) + str(a1)):
                return True
            else:
                return False

        for i in range(len(nums)-1):
            for j in range(len(nums)-1 - i):
                if not compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print(nums)
        answer = ''
        for k in range(len(nums) - 1, -1, -1):
            answer += str(nums[k])
        if answer.startswith('0'):
            return "0"
        return answer


sol = Solution()
print(sol.largestNumber([5, 9, 3, 30, 34]))
