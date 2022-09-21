def recursive(i):
    if i == 100:
        return
    print(i, '->', i + 1)
    recursive(i + 1)
    print('종료', i)


recursive(1)
