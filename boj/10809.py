import string

word = input()
result = [-1] * len(string.ascii_lowercase)
for i in range(len(word)):
    val = ord(word[i]) - ord('a')  # 문자를 숫자로 변환하는 함수
    if result[val] == -1:
        result[val] = i
print(' '.join([str(word) for word in result]))
