class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class NodeDataBase:
    def __init__(self):
        self.node=[]
    # def insert(self,nod):
    #     if(len(self.node)==0):
    #         self.node.insert(nod)
    #     else:
    #         tree=node
    #         while
def parse_binary_search_tree(data):
    if(isinstance(data,tuple) and len(data)==3):
        node=Node(data[1])
        node.left=parse_binary_search_tree(data[0])
        node.right=parse_binary_search_tree(data[2])
    elif(data is None):
        node=None
    else:
        node=Node(data)
    return node

def tree_to_tuple(node,tup,level=0):
    if(node is None):
        print('\t'*level)
    else:
        tup=node.key
        tree_to_tuple(node.right,tup,level+1)
        print( '\t'*level,end='')
        print(tup,end=' ')
        tree_to_tuple(node.left,tup,level+1)





data=((None,2,3),4,((5,6,8),7,(6,8,None)))


tree=parse_binary_search_tree(data)
tree_to_tuple(tree,(),level=0)
# print(tree.right.left.key)
