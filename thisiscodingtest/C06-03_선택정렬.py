array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array) - 1):
    minidx, minval = i, array[i]
    for a in range(i + 1, len(array)):
        if minval >= array[a]:
            minidx = a
            minval = array[a]
    array[minidx], array[i] = array[i], array[minidx]

print(array)
