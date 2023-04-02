import random
import time

def naivesearch(l,target):
    #example l = [1,3,10,12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binarysearch(l, target, low=None, high=None):
    if low is None:
        low =0
    if high is None:
        high =len(l) - 1
    if high < low:
        return -1
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binarysearch(l, target, low, midpoint-1)
    else:
        return binarysearch(l, target, midpoint+1, high)
if __name__=='__main__':
    l =[1,3,5,10]
    target =10
    print(naivesearch(l, target))
    print(binarysearch(l, target))
    length = 1000
    sortedlist =set()
    while len(sortedlist) <length:
        sortedlist.add(random.randint(-3*length, 3*length))
    sortedlist = sorted(list(sortedlist))

    start = time.time()
    for target in sortedlist:
        naivesearch(sortedlist, target)
    end = time.time()
    print("Naive search time", (end-start), "seconds")

    start = time.time()
    for target in sortedlist:
        binarysearch(sortedlist, target)
    end = time.time()
    print("Binary search time", (end-start), "seconds")