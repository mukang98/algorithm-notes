# %%
# ================================================================= #
#                        1.Decorator                                #
# ================================================================= #
#In Python, Decorator is a special type of function that can modify or enhance the functionality of other functions rather than change its original code.
# Decorators are marked with @ symbol before function definiton. They allow you add addtional functionalities in a declarative way, 
# such as performance monitoring, model saving and loading, logging, etc.
import time 
def time_decorator(func):
#accept 'func' as input
    def wrapper(*args, **kwargs):
    #'*args' and '**kwargs' are used to accommodate any inputs.       
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} executed in {end_time - start_time} seconds')
    return wrapper

@time_decorator
def say_hello(name):
    time.sleep(2)
    print(f'Good morning, {name}!')

say_hello('Wayne')
#%%
# ================================================================= #
#                        1.1 Property Decorator                     #
# ================================================================= #
#Property decorater allows developer to accesss a class method as if it were an attribute.
#It can make the code more concise and easier to understand and maintain, while enhancing data encapsulation and security.
class Person:
    def __init__(self, name):
        self._name = name  # "_" represents _name is a protected attribute

    @property
    def set_name(self):
        """Getter method, return _name attribute value"""
        return self._name

    @set_name.setter
    def set_name(self, value):
        """Setter method, set the value of _name attribute"""
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @set_name.deleter
    def set_name(self):
        """Deleter method, delete the _name attribute"""
        del self._name

person = Person("wayne")
#%%
#Accsess this class method as if it were a attribute.
print(person.set_name) #wayne 
#%%
#Change the protected attribute
person.set_name = "Bob"
print(person.set_name) #Bob
#%%
#In this case, .setter does concrete limitation on assignment of the attribute to ensure the security.
person.set_name = 123 
print(person.set_name) #ValueError: Name must be a non-empty string
#%%
#delete the protected attribute
del person.set_name
#%%
#In thic case, property decorater reduce the number of explicit attributes making the code more concise.
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# e.g.
circle = Circle(5)
print("Radius:", circle.radius)  # output: Radius: 5
print("Diameter:", circle.diameter)  # output: Diameter: 10
print("Area:", circle.area) #output: Area: 78.53975

