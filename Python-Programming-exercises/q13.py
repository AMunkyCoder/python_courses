# Question 13
# Level 2
# Question: Write a program that accepts a sentence 
# and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: 
# hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
# 
# Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input.
# 

# Solution
def sol():
    s = input()
    d={"DIGITS":0, "LETTERS":0}
    for c in s:
        if c.isdigit():
            d["DIGITS"]+=1
        elif c.isalpha():
            d["LETTERS"]+=1
        else:
            pass
    print("LETTERS", d["LETTERS"])
    print("DIGITS", d["DIGITS"])


# My Code
def sentences():
    sen = input()
    word = 0
    num = 0
    for s in sen:
        if s.isalpha() == True:
            word += 1
        elif s.isnumeric() == True:
            num += 1
        else:
            pass
    print("LETTERS %i DIGITS %i" % (word, num))


if __name__ == "__main__":
    sentences()