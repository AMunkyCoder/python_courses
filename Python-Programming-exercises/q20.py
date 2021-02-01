# Question 20
# Level 3
# Question: Define a class with a generator which 
# can iterate the numbers, which are divisible by 7, 
# between a given range 0 and n.
# 
# Hints: Consider use yield

# Solution
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

############################## Uncomment this
# for i in putNumbers(100):
#     print(i)
##############################

# My Code
class MyGen:
    def __init__(self, num):
        self.num = num


    def generator(self):
        terator = 0
        while terator < self.num:
            div = terator
            terator = terator + 1
            if div % 7 == 0:
                yield div


if __name__ == "__main__":
    gen = MyGen(100)
    gen.generator()
    for value in gen.generator():
        print(value)
    # putNumbers(100)