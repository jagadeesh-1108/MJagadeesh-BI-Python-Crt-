'''s = input("Enter a string: ")
result = ""
sp = s[0]
count = 1
for i in range(1, len(s)):
    if s[i] == sp:
        count += 1
    else:
        result += sp + str(count)
        sp = s[i]
        count = 1
result += sp + str(count)
print(result)'''
s=input("enter the string: ")
res=''
for ch in s:
    if ch not in res:
        res += ch + str(s.count(ch))
print(res)        
