'''n=int(input())
if n%2==0:
    if n>=1:
        print("Number is positive even")
    else:
        print("Number is negative even")
else: 
    if n>=1:
        print("Number is positive odd")
    else:
        print("Number is negative odd")'''

#check which one is even number or odd number in the given list of numbers
'''lst=[2,4,3,5,6,7,9]
for num in lst:
    if num%2==0:
        print(num, "is even")
    else:
        print(num,"is odd")
print("program done")'''

#check which one is +ve number or -ve number in the given list of numbers
lst=[2,4,-3,5,-6,-7,9]
for num in lst:
    if num>=0:
        print(num, "is +ve")
    else:
        print(num,"is -ve")
print("program done")

#print 1 to 20numbers using range function
for num in range(1,21,1):
    print(num)

#print even numbers in between 0-20 using range function
for num in range(0,21,2):
    print(num, end=",") #if we want it to be printed horizontally 
    
