# Question 1
# Level 1
# Question: Write a program which will find all such numbers
# which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated
# sequence on a single line.
#
# Hints: Consider use range(#begin, #end) method

# Solution
def sol():
    l=[]
    for i in range(2000, 3201):
        if (i%7==0) and (i%5!=0):
            l.append(str(i))

    print(','.join(l))


# My Code
def div_by_seven():
    num = []
    for div in range(2000, 3201):
        if (div % 7 == 0) and (div % 5 != 0):
            num.append(str(div))

    print(','.join(num))

if __name__ == '__main__':
    div_by_seven()