#reverce string without slicing
s=input()
rev = "" 
for ch in s:
    rev=ch[0]+rev
print(rev)

# s=input()
# rev = ""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# print(rev)