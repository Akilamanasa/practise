#valid Pandrom(Leetcode)
s = input("Enter a string: ")
s = ''.join(c.lower() for c in s if c.isalnum())
i,j=0,len(s)-1
while i<=j:
    if s[i]!=s[j]:
        print(False)
        break
    i+=1
    j-=1
else:
    print(True)
