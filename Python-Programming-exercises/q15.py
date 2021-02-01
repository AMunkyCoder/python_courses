# Question 15
# Level 2
# Question: Write a program that computes the value of a+aa+aaa+aaaa 
# with a given digit as the value of a. Suppose the following input is 
# supplied to the program: 9 Then, the output should be: 11106
# 
# Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input.

# Solution
def sol():
    a = input()
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    n4 = int( "%s%s%s%s" % (a,a,a,a) )
    print(n1+n2+n3+n4)


# My Code
def compute():
    num = input()
    # pattern = "a+aa+aaa+aaaa"
    pattern, n = 5, 0
    stnum = []
    for patt in range(1, pattern):
        stnum.append(patt * str(num))
    for s in stnum:
        n += int(s)
    print(n)


if __name__ == "__main__":
    compute()