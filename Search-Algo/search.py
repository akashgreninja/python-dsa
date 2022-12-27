import math

def linearsearch(list,element):
    for i in list:
        if i==element:
            return "found it"
        else:
            continue
    return "not there"

def BinarySearch(list,value):
    start=0
    end=len(list)-1
    middle=math.floor((start/end)/2)
    while not (list[middle]==value):
        if value<list[middle]:
            end=middle-1
        else:
            start =middle+1

        middle=math.floor((start+end)/2)
        print(start,middle,end)
    return middle



list=[1,4,5,6,2,3,9]
# print(linearsearch(list,5))
print(BinarySearch(list,5))