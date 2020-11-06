# yeah gonna skip making pong it's just a bunch of turtle nonsense

class Animal():
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")


# Class inheritance
class Fish(Animal):
    def __init(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    # inherit then modify method
    def breathe(self):
        super().breathe()
        print("doing this underwater")


nemo = Fish()
nemo.swim()
nemo.breathe()