from llist import LList, Node, append
import random

def length(lst):
    """return the length of a finite linked list"""
    curr,count=lst.head,0
    while(curr):
        count+=1
        curr=curr.next
    return count
    


def llprint(lst):
    """print a finite linked list"""
    curr=lst.head
    while(curr):
        print(curr.val,end=" ")
        curr=curr.next
    print()


if __name__ == "__main__":

    myLlist = LList()
    for i in range(10):
        append(myLlist, Node(2 ** i))

    print(length(myLlist))
    llprint(myLlist)

    emptyList = LList()
    print(length(emptyList))
    llprint(emptyList)

    testNums = [random.randint(0, 1000) for a in range(20)]
    print(testNums)

    llist2 = LList()
    for i in testNums:
        append(llist2,Node(i))
    print(length(llist2))
    llprint(llist2)

    from genfinite import lst
    print(length(lst))
