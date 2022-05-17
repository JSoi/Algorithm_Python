def garo(thisline):
    arr = list(thisline)
    cnt = 0
    stk = []
    for i in arr:
        if i == '(':
            stk.append('(')
            cnt += 1
        else:
            if not stk:
                return False
            if stk[-1] != '(':
                return False
            else:
                cnt -= 1
                stk.pop()
    if len(stk) > 0:
        return False
    return True


count = input()
answer = ""

for i in range(int(count)):
    thisline = input()
    if garo(thisline):
        answer += "YES\n"
    else:
        answer += "NO\n"
print(answer)



