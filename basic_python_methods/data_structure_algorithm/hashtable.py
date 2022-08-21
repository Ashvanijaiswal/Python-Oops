class HashTable:
    def __init__(self,size):
        self.size=size
        self.arr=[]



    def _hash(self,key):
        hash=0
        for i in range(0,len(key)):
            hash=(hash+ord(key[i])*i)%self.size
        return hash

    def set(self,key,value):
        address=self._hash(key)
        if(len(self.arr)==0):
            self.arr.append([0]*self.size)
        # self.arr[address].append([key,value])
        print(self.arr)
        return self.arr

    def get(self,key):
        address=self._hash(key)


hs=HashTable(2)
hs.set('grapes',1000)
hs.set('grapesss',100001)
