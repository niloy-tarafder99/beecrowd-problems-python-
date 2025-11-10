val = int(input())

t = [3600,60,1]
ans = []

for i in t:
    quotient = int(val/i)
    ans.append(quotient) #this function sending value from quotient to ans
    reminder = val%i
    val = reminder

print(f'{ans[0]}:{ans[1]}:{ans[2]}')
