# <--- INHERITANCE QUICK GUIDE --->
# OVERVIEW: A "sub class"(or "child" class) can inherit attributes and methods from a "super class"(or "parent" class)  but can also define new attributes and methods of its own.


# <--- __init__() Method For Sub Class --->
# DESCRIPTION: This will initialize any attributes that were defined in the parent __init__() method and make them available to the child class.


# <--- NB. --->
# (1) Parents classes must precede child classes in the file.


# <--- CODE --->

class SuperClass:
    """Initialize attributes of SuperClass."""
    def __init__(self, attrib_1, attrib_2, attrib_3):
        self.attrib_1 = attrib_1
        self.attrib_2 = attrib_2
        self.attrib_3 = attrib_3

    def list_attrib_1(self):
            print(f'{self.attrib_1} is the value of attrib_1 for {self}.')
    
class SubClass(SuperClass):
        
    def __init__(self, attrib_1, attrib_2, attrib_3):
        """Initialize attributes of the SuperClass."""
        super().__init__(attrib_1, attrib_2, attrib_3)
        """Initialize attributes unique to SubClass."""
        self.attrib_4 = 7

# <--- Create Instances --->
parent = SuperClass(1, 2, 3)
child = SubClass(4, 5, 6)

# <--- Call Methods From Both Instances --->
parent.list_attrib_1()
child.list_attrib_1()
print(f'{child.attrib_4} is the value of attrib_4 in {child}')
