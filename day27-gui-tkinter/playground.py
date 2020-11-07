#unlimited args
def add(*args):
    print(args[1]) # 5
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,7))
print(add(3,5,7,3,4,6,7,4,2,3,5,7,8,9))

# kwargs
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.transmission = kw.get("transmission")

my_car = Car(make="Nissan", model="370z")
print(my_car.model) # nissan
print(my_car.transmission) # None

