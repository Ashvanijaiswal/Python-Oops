class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        sel f.head=None
        self.length=0

    def add_item(self,item):
        self.node=Node(item)
        if self.head==None:
            self.head=self.node
            return
        current=self.head
        while current.next!=None:
            current=current.next

        current.next=self.node
        self.length+=1

    def remove(self):
        if(self.head==None or self.length==0):
            print('Empty LikedList')
            return
        current=self.head
        while current.next.next!=None:
            current=current.next
        current.next=None
        self.length-=1

    def lengt(self):
        return self.length
    def remove_list(self):
        self.head=None

    def find(self,item):
        if(self.length==0 or self.head==None):
            return None
        c=-1
        current=self.head
        while current!=None:
            if(current.data==item):
                return c+1
            current=current.next
            c+=1
        return -1



    def list_items(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
