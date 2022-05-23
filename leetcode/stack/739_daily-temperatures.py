from typing import List


class Solution_timeout:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        answer = []
        for i in range(len(temperatures)):
            tlist = []
            for j in range(i + 1, len(temperatures)):
                tlist.append(temperatures[j])
                if temperatures[j] > temperatures[i]:
                    break
            print(len(temperatures) - i - 1, len(tlist))
            if len(temperatures) - i - 1 < len(tlist):
                answer.append(0)
                continue
            elif len(temperatures) - i - 1 == len(tlist):
                if len(tlist) > 0 and tlist[-1] <= temperatures[i]:
                    answer.append(0)
                    continue
            answer.append(len(tlist))
        print(answer)
        return answer

    # temperatures = [34,80,80,80,34,80,80,80,34,34]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures): # i는 0 부터, cur는 i번째 value
            while stack and cur > temperatures[stack[-1]]: # stack의 마지막 값이 현재 값보다 작은지 확인
                last = stack.pop() # 작다면 증가한 것이므로 업데이트 해줘야 한다
                answer[last] = i - last
            stack.append(i)
        return answer


temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
sol = Solution()
print(sol.dailyTemperatures(temperatures))
