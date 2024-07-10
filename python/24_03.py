"""
Some Python skills and knowledge 
"""
# ================================================================= #
#                        1.Fancy Indexing                           #
# ================================================================= #
# Fancy Indexing is an advanced indexing method in Numpy, which is still available in pytorch.
#%%
#Import needed library
import numpy as np
#%%
#Usage 1 : 1-D Arrays
#Create a 1-D array
a = np.arange(10)
#Using fancy indexing
chosen_a = a[[0, 3, 7]] #[0 3 7]
print(chosen_a)
# %%
#Usage 2 : 2-D Arrays
#Create a 2-D array
b = np.arange(24).reshape(4,6)
print(b)
#Using fancy indexing
chosen_b = b[[1,2],[3,4]] #[ 9 16]
print(chosen_b)
# %%
#Usage 3: Mixing fancy indexing and Slicing
#Using fancy indexing
chosen_b_mix = b[1:3,[3,4]] #[[9 10],[15 16]]
print(chosen_b_mix)
# %%
#Usage 4: Bool indexing
#Create a bool array
bool_index = a % 2 == 0 #[ True False  True False  True False  True False  True False]
#Using fancy indexing
chosen_a_bool = a[bool_index] #[0 2 4 6 8]
# %%
# ================================================================= #
#                        2.Property Decorator                       #
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

