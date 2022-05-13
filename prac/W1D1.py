import string
from pprint import pprint

text = 'hello, this is sparta'

counter = {}
# 21 번 연산
for char in text:
    if not char.isalpha():
        continue
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1
pprint(counter)

counter2 = {}
# 26 * 21 번 연산
for lo in string.ascii_lowercase:
    for char in text:
        if lo == char:
            if lo in counter2:
                counter2[lo] += 1
            else:
                counter2[lo] = 1
pprint(counter2)

list = [3, 5, 6, 1, 2, 4]
max = list[0]
for i in list:
    if max < i:
        max = i
pprint(max)

my_list = [3, 5, 6, 1, 2, 4]


def find(arr, x):
    for i in my_list:
        if i == x:
            return True
    return False


print(find(my_list,4))
