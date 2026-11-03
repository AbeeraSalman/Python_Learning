class A:
    def meow(self):
        print("meow")
class B:
    def meow(self):
        print("meow1")

class C(A,B):
    pass

obj=C()
obj.meow()


