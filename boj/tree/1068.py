
a = int(input())
mylist = list(map(int, input().split()))
remove = int(input())

# 리프노드라 하면은... 자식이 없는 것을 뜻함


conn = dict()
for i in range(-1, a):
    conn[i] = list()
for i in range(len(mylist)):
    conn[mylist[i]].append(i)


def delete(ele):
    for l in conn[ele]:
        delete(l)
    del conn[ele]


if mylist[remove] == -1:
    print(0)
else:

    # dictionary에서 삭제하고
    # 삭제하기 전에 해당 리스트의 값을 연쇄적으로 삭제해주어야 한다.
    # print(conn)
    delete(remove)
    for d in conn:
        if remove in conn[d]:
            conn[d].remove(remove)
    count = 0
    for d in conn:
        if len(conn[d]) == 0:
            count += 1
    print(count)
