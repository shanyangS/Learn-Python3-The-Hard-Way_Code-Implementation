## Animal is-a object (yes,sort of confusing) look at the extra credit (附加练习)
class Animal(object):
    pass

## is-a
class Dog(Animal):

    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Cat(Animal):

    def __init__(self, name):
        ## has-a
        self.name = name

## is-a
class Person(object)

    def __init__(self, name):
        ## has-a
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## has-a hmm what is this strange magic? super()是一个内置函数，用于调用父类（也称为超类）的方法。它常用于重写（override）或扩展（extend）继承自父类的方法。super()的使用非常频繁在面向对象编程中，尤其是在有继承关系的类中。
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## frank is a employee
frank = Employee("Frank", 120000)

## frank has-a pet called satan
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()