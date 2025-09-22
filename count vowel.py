#count vowel
s=input()
c=0
v='aeiouAEIOU'
for char in s:
    if char  in v:
        c+=1
print(c)