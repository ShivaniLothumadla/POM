class A:
    # pass
    def display(self):
        print('display from class A.')

class B(A):
    def display(self):
        super(B, self).display()
        print('display from class B.')

class C(B):
    def show(self):
        print('show from C.')

class D(C):
    def show(self):
        super(D, self).show()
        print('show from D.')


obj = D()
obj.show()