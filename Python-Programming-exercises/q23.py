# Question 23
# level 1
# Question: Write a method which can calculate square value of number
# 
# Hints: Using the ** operator

# Solution
def sol():
    def square(num):
        return num ** 2

    print(square(2))
    print(square(3))


# My Code
class MyMath():
    def __init__(self, sq):
        self.sq = sq
    
    def calcsq(self):
        return self.sq ** 2

if __name__ == "__main__":
    sq = MyMath(3)
    print(sq.calcsq())
    # sol()