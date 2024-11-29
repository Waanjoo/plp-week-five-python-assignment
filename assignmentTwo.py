class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Dog is running")

class Bird(Animal):
    def move(self):
        print("Bird is flying")

class Fish(Animal):
    def move(self):
        print("Fish is swimming")

# Create objects of different animal classes
dog = Dog()
bird = Bird()
fish = Fish()

# Call the move method on each object
dog.move()
bird.move()
fish.move()