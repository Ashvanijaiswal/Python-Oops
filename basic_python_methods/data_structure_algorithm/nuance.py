class A(object):
 
    def hi(self):
        print("Greetings to every one")
 
    def start(self):
        self.hi()
        print("Lets start the meeting")
 
 
class B(A):
 
    def total(self):
        print("the total audience is more than expected")
 
    def hi(self):
        print("Thank you for joining us")
 
 
b = B()
b.start()
print(help(b))