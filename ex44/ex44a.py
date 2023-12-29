class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass
# 隐式继承（Implicit Inheritance）
dad = Parent()
son = Child()

dad.implicit()
son.implicit()