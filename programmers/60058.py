def solution(p):
    answer = ''

    def balanced(string):
        if string.count('(') == string.count(')'):  # 균형잡힌
            return True
        else:
            return False

    def correct(string):
        if not balanced(string):
            return False
        garo = 0
        for i in range(len(string)):
            now = string[i]
            if now == '(':
                garo += 1
            elif now == ')':
                garo -= 1
            if garo < 0:
                return False
        if garo != 0:
            return False
        return True

    def trimandreverse(string):
        trimstring = string[1:len(string) - 1]
        a = ''
        for i in trimstring:
            if i == ')':
                a += '('
            else:
                a += ')'
        return a

    if len(p) == 0 or correct(p):
        return p
    for i in range(1, len(p) + 1):
        u, v = p[:i], p[i:]
        if balanced(u) and balanced(v):
            if not correct(u):
                return '(' + solution(v) + ')' + trimandreverse(u)
            else:
                return u + solution(v)
    return answer
