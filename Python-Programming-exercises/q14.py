# Question 14
# Level 2
# Question: Write a program that accepts a sentence 
# and calculate the number of upper case letters 
# and lower case letters. Suppose the following input 
# is supplied to the program: Hello world! Then, 
# the output should be: UPPER CASE 1 LOWER CASE 9
# 
# Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input.

# Solution
def sol():
    s = input()
    d={"UPPER CASE":0, "LOWER CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER CASE"]+=1
        elif c.islower():
            d["LOWER CASE"]+=1
        else:
            pass
    print("UPPER CASE", d["UPPER CASE"])
    print("LOWER CASE", d["LOWER CASE"])

# My Code
def sentences():
    sen = input()
    sentence = {'upper': 0, 'lower': 0}
    for s in sen:
        if s.islower():
            sentence['lower'] += 1
        elif s.isupper():
            sentence['upper'] += 1
        else:
            pass
    print("UPPER CASE ", sentence['upper'], "LOWER CASE ", sentence['lower'] )

if __name__ == "__main__":
    sentences()