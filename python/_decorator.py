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
    def name(self):
        """Getter method, return _name attribute value"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter method, set the value of _name attribute"""
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @name.deleter
    def name(self):
        #在 Python 中使用 @property 装饰器时，getter、setter 和 deleter 方法的名字必须和属性名一致。
        """Deleter method, delete the _name attribute"""
        del self._name

person = Person("wayne")
#%%
#Accsess this class method as if it were a attribute.
print(person.name) #Accsess the 'name' attribute using the property getter. This protects the _name attribute by not allowing direct access.
#%%
#Change the protected attribute
person.name = "Bob"
print(person.name) #Bob
#%%
#In this case, .setter does concrete limitation on assignment of the attribute to ensure the security.
person.name = 123 
print(person.name) #ValueError: Name must be a non-empty string
#%%
#delete the protected attribute
del person.name
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

