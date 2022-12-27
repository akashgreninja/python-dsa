def swap (list ,index1,index2):
    list[index1],list[index2]=list[index2],list[index1]

def pivot(list,pivot_index,last_index):
    swap_index=pivot_index
    for i in range(swap_index+1,last_index+1):
        if list[i]< list[pivot_index]:
            swap_index+=1
            swap(list,swap_index,i)
    swap(list,pivot_index,swap_index)
    return swap_index

def quicksort(list,l,r):
    if l<r:
        pivot_index=pivot(list,l,r)
        quicksort(list,l,pivot_index-1)
        quicksort(list,pivot_index+1,r)

    return list



def heapify(customList,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and customList[l]< customList[smallest]:
        smallest=l
    if r<n and customList[r]< customList[smallest]:
        smallest=r
    if smallest!= i:
        customList[i],customList[smallest]=customList[smallest],customList[i]
        heapify(customList,n,smallest)
    


def heapsort(customList):
    n=len(customList)
    for i in range(int(n/2)-1,-1,-1):
        heapify(customList,n,i)

    for i in range (n-1,0,-1):
        customList[i],customList[0]=customList[0],customList[i]
        heapify(customList,i,0) 


list=[3,5,0,6,2,1,4]
print(quicksort(list,0,6))
heapsort(list)
print(list)