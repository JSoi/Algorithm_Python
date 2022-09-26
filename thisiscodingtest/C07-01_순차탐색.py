array = ['Dongbin', 'Taeil', 'Sangwook']


def seq_search(target):
    for i in range(len(array)):
        if array[i] == target:
            return i + 1


print(seq_search('Taeil'))
