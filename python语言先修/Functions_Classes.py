# Functions & Classes

def my_function(a,b,c):
    print(a+b+c)

# TypeHint
def my_function2(a:int,b,c: int = 1):
    print(a+b+c)
    return c
a = my_function2(1,2,3)
print(a)

my_function(1.0,2,4) # 不检查

class MyClass:
    def __init__(self,name = 'acm',number = 10):
        self._name = name #protected 的补救措施
        self.number = number

    def print_inf(self):
        print(self.number)

student = MyClass(number=20)
print(student._name)
student.print_inf()