class Animal:
    shape = ""
    gender = ""
    color = ""
    height = 0.0
    volume = 0.0
    age = 0
    sound = ""
    species = ""

    def __init__(self, shape, gender, color, height, volume, age, sound, species):
        self.shape = shape
        self.gender = gender
        self.color = color 
        self.height = height
        self.height = height
        self.volume = volume
        self.age = age
        self.sound = sound
        self.species = species
        pass

    def speak(self):
        print ("Noise")
    
    def eat(self):
        print("much")
    
    def sleep(self):
        print("Zzzz")

animal1 = Animal("circle","male", "brown", 1.1, "meow", 3.3, 2, "dog")
print(animal1.species)

#Inheritance: