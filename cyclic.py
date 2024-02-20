from llist import *

def llprint(lst, num):
    node,count=lst.head,0
    while(node and count < num):
        print(node.val,end=" ")
        node=node.next
        count+=1
    print()

def find_cycle(lst):
    """return the start index and length of the cycle"""
    pass

def buildList(n): #generate a cyclic list of length n
    lst = LList()
    for i in range(n):
        if(i < 10):
            append(lst, Node(2 ** i))
        else: 
            power = 10 + (i % 5)
            append(lst, Node(2 ** power))
    return lst

if __name__ == "__main__":
    myList = buildList(25)
    
    find_cycle(myList)

    llprint(myList, 10)
