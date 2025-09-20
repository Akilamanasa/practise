#The number should be end with 7 and divide by 7
n=int(input())
if n%7==0 or n%10==7:
    print("buz")
else:
    print("not buzzz")