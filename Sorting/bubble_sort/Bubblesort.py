
def BubbleList(list):
    for _ in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    print(list)            
        

# here we see which is the minimum among the list and put it to the left and keep doing it 
def selectionSort(list):
    for i in range(len(list)):
        # min_value=i
        for j in range(i+1,len(list)):
            if list[i]> list[j]:
                list[j],list[i]=list[i],list[j]
        # list[min_value],list[i]=list[i],list[min_value]
    print(list)


# def InsertionSort(list):
#     check=[]
#     for i in range(len(list)):
#         for j in check:
#             if i > j:
#                 check[j+1]=i
#             else:
#                 check[1]=j
#     print(check)



def InsertionSort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and key < list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=key
    print(list)


# BubbleList([4,1,3,7,2])
# selectionSort([4,1,3,7,2])
InsertionSort([4,1,3,7,2])