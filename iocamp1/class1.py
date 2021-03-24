class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
class BullDog(Dog):
    def run(self,speed):
        return "{} runs {}" .format(self.name,speed)
class Shitzu(Dog):
    def run(self,speed):
        return "{} runs {}" .format(self.name,speed)


# Instantiate the Dog object
jim=BullDog("Jim",12)
print(jim.description())
print(jim.run("slowly"))

print(isinstance(jim,Dog))

julie=Dog("Julie",100)
print((isinstance(julie,Dog)))