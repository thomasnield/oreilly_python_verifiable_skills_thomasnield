class A:  
    def do_action(self):  
        print("In class A")  
  
class B(A):  
    def do_action(self):  
        print("In class B")  
  
class C(A):  
    def do_action(self):  
        print("In class C")  
  
class D(B,C):  
    def do_action(self):
	    super.do_action()
  
r = D()  
r.do_action() # prints "In class B"