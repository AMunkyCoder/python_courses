# Question 25
# Level 1
# Question: Define a class, which have a class 
# parameter and have a same instance parameter.
# 
# Hints: Define a instance parameter, 
# need add it in init method You can init a object 
# with construct parameter or set the value later


# Solution
class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

def sol():
    jeffrey = Person("Jeffrey")
    print("%s name is %s" % (Person.name, jeffrey.name))

    nico = Person()
    nico.name = "Nico"
    print("%s name is %s" % (Person.name, nico.name))

# My Code
class Person:
    """
    docstring
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
def callingclass():
    P1 = Person("Allison", 25)
    print(P1.name)


if __name__ == "__main__":
    callingclass()