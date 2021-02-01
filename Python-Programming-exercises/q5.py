# Question 5
# Level 1
# Question: Define a class which has at least two methods: 
# getString: to get a string from console input printString: 
# to print the string in upper case. Also please include 
# simple test function to test the class methods.
# 
# Hints: Use init method to construct some parameters

# Solution
# Author didn't include an answer to the test function
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

# Uncomment this.

# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
#############################

# My Code
class myClass:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = str(input())
    
    def printString(self):
        return self.text.upper()


def test_string():
    text = myClass()
    text.getString()
    assert text.printString() == "PUT STRING HERE"

if __name__ == "__main__":
    test_string()