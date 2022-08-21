class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedListImpl:
    def __init__(self):
        self.head=None

    def insert(self,data):
        if(self.head==None):
            self.head=Node(data)
        else:
            node=self.head
            while(node.next!=None):
                node=node.next
            node.next=Node(data)

    def show_result(self):
        node=self.head
        while(node!=None):
            print(node.data,end=' ')
            node=node.next
        print()
    def remove_duplicate(self):
        node=self.head
        l2=LinkedListImpl()
        s=set()
        while(node.next!=None):
            if(node.data not in s):
                s.add(node.data)
                l2.insert(node.data)
            node=node.next
        return l2
    def reverse(self):
        prev=self.head
        cur=self.head
        if(cur.next==None):
            return

        prev.next=cur.next
        cur.next=prev
        self.head=cur
        self.reverse()
        return self

l=LinkedListImpl()
for i in range(0,2):
    l.insert(i)
l.show_result()
print(l.reverse().show_result())
# l.remove_duplicate().show_result()
