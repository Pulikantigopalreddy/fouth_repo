class A:
    def add(self, x, y):
        return x + y


class B(A):
    def sub(self, x, y):
        return x - y


class C(B):
    def mul(self, x, y):
        return x * y


class D(C):
    def div(self, x, y):
        return x / y


inst_obj = D()
print(inst_obj.add(20, 30))
print(inst_obj.sub(20, 30))
print(inst_obj.mul(20, 30))
print(inst_obj.div(20, 30))