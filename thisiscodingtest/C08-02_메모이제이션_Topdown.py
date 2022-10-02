mylist = [0] * 100

mylist[1] = mylist[2] = 1
n = 99
for i in range(3, n+1):
    mylist[i] = mylist[i-1] + mylist[i-2]

print(mylist[n])