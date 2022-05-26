import sys

cnt = int(sys.stdin.readline().rstrip())
answer = ''

for _ in range(cnt):
    numbercnt = int(sys.stdin.readline().rstrip())
    numbers = []

    for _ in range(numbercnt):
        numbers.append(sys.stdin.readline().rstrip())
    numbers.sort()


    def compare(nums):
        for i in range(len(nums) - 1):
            if str(nums[i + 1]).startswith(nums[i]):
                return 'NO\n'
        return 'YES\n'


    answer += compare(numbers)
print(answer)
