age = int(input())

arr = [365,30,1]
text = ['ano(s)','mes(es)','dia(s)']
ans =[]

for i in arr:
    quotient = int(age/i)
    ans.append(quotient)
    remimder = age%i
    age = remimder

for i in range(3):
    print(f'{ans[i]} {text[i]}')