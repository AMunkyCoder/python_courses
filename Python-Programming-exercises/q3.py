# Question 3
# Level 1
# Question: With a given integral number n, 
# write a program to generate a dictionary 
# that contains (i, i*i) such that is an 
# integral number between 1 and n (both included). 
# and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 
# 8 Then, the output should be: 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# 
# Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input. Consider use dict()

# Solution
def sol(num): # added num to test my code if correct.
    # n=int(input()) # uncomment this one, it's from the original solution
    d=dict()
    for i in range(1,num+1):
        d[i]=i*i

    print(d)


# My Code
def integ(num):
    integraldict = {}
    for i in range(1, num + 1):
        integraldict[i] = i * i
    
    return integraldict  


if __name__ == "__main__":
    num = int(input())
    print(integ(num))
    sol(num)