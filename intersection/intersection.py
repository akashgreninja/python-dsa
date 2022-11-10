from LinkedList import SingleLinkedList, Node


def interection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False

    lenA = len(ll1)
    lenB = len(ll2)
    shorter = ll1 if lenA < lenB else ll2
    longer = ll2 if lenA < lenB else ll1

    diff = len(longer)-len(shorter)

    longernode = longer.head
    shorternode = shorter.head

    for i in range(diff):
        longernode = longernode.next

    while shorternode is not longernode:
        shorternode = shorternode.next
        longernode = longernode.next

    return longernode


def addsameNode(ll1, ll2, value):
    temp = Node(value)
    ll1.tail.next = temp
    ll1.tail = temp
    ll2.tail.next = temp
    ll2.tail = temp


ll1 = SingleLinkedList()
ll1.randomvar(3, 0, 10)


ll2 = SingleLinkedList()
ll2.randomvar(3, 0, 10)


addsameNode(ll1, ll2, 9)
# addsameNode(ll1,ll2,14)

print(ll1)
print(ll2)
print(interection(ll1, ll2))
