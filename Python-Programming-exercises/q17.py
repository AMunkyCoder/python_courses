# Question 17
# Level 2
# Question: Write a program that computes the net amount 
# of a bank account based a transaction log from console input. 
# The transaction log format is shown as following: D 100 W 200
# D means deposit while W means withdrawal. 
# Suppose the following input is supplied to the program: 
# D 300 D 300 W 200 D 100 Then, the output should be: 500
# 
# Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input.
# 
# 
# Solution
def sol():
    netAmount = 0
    while True:
        s = input()
        if not s:
            break
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation=="D":
            netAmount+=amount
        elif operation=="W":
            netAmount-=amount
        else:
            pass
    print(netAmount)


# My Code
def computes():
    net_amount = 0

    while True:
        transaction = input("[D] Deposit [W] Withdraw [Q] Exit <space> amount 'D 1000': ")
        option = transaction[0].upper()
        if option == 'D':
            net_amount += int(transaction[2:])
        elif option == 'W':
            net_amount -= int(transaction[2:])
        elif option == 'Q':
            break
        else:
            print("Not applicable")
        print("Total Balance is: %i" % (net_amount))


if __name__ == "__main__":
    computes()