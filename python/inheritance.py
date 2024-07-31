# ================================================================= #
#                        1.Inheritance                              #
# ================================================================= # 
#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (known as a subclass or derived class) 
# to inherit attributes and methods from another class (known as a superclass or base class). 
# This promotes code reusability and allows for the creation of hierarchical class structures.
#%%
"""
Define the Base Class
"""
class Animal:
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def info(self):
        return f'Animal: {self.name}'
#%%
"""
Define the Derived Class
"""
class Dog(Animal):
    def speak(self):
        return "Woo"
    def info(self):
        return f"Dog: {self.name}" #Method Overriding
dog = Dog("Buddy")
print(dog.speak())
print(dog.info())
# %%
"""
Using 'super()'
"""
#The super() function allows you to call methods from the base class within the derived class. 
# This is useful when you want to extend the functionality of the base class method rather than completely overriding it.
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly
    
    def speak(self):
        return "GiGi"
    
    def info(self):
        base_info = super().info()
        return f'{base_info} and it {self.can_fly} fly'
bird = Bird("Lucky","can")
print(bird.info())

# %%
