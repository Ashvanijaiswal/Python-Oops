from linked_list_impl import *
if __name__=='__main__':
    l1=LinkedList()
    l1.add_item(1)
    l1.add_item(2)
    l1.add_item(4)
    l1.add_item(5)
    print('length of list is:',l1.lengt())
    l1.list_items()
    print("Elemnet present at:",l1.find(0))
