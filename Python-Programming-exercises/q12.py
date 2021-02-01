# Question 12
# Level 2
# Question: Write a program, which will 
# find all such numbers between 1000 and 3000 
# (both included) such that each digit of the number 
# is an even number. The numbers obtained should be 
# printed in a comma-separated sequence on a single line.
# 
# Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input.

# Solution
def sol():
    values = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
            values.append(s)
    print(",".join(values))


# My Answer
def evens():
    # even = [str(e) for e in range(1000, 3001) if e % 2 == 0]
    # print(",".join(even))
    even = []
    for e in range(1000, 3001):
        num = str(e)
        if (int(num[0]) % 2 == 0) and (int(num[1]) % 2 == 0) and (int(num[2]) % 2 == 0) and (int(num[3]) % 2 == 0):
            even.append(num)
    print(",".join(even))

if __name__ == "__main__":
    evens()
    # sol()