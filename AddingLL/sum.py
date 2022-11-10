from LinkedList import SingleLinkedList

def sumlist(ll1,ll2):
    no1=ll1.head
    no2=ll2.head
    carry=0
    linked=SingleLinkedList()
    while no1 or no2:
        result=carry
        if no1:
            result+=no1.value
            no1=no1.next
        if no2:
            result+=no2.value
            no2=no2.next
        linked.add(result%10)
        carry=result// 10
    if carry>0:
        linked.add(int(carry))
    return linked


ll1=SingleLinkedList()
ll1.add(2)
ll1.add(3)
ll1.add(7)


ll2=SingleLinkedList()
ll2.add(9)
ll2.add(3)
ll2.add(7)

print(ll1)
print(ll2)

print(sumlist(ll1,ll2))
        

