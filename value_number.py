"""# check the value number

n=10
if n<=0 and n%2==0:
    print("enter the positive value is:",)
elif n>=0 and n%2==0:
    print("enter the negitive value:",)
elif n==0:
    print("enter the zero value:",)
else:
    print("enter the actual number value:",)"""




def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
