val = int(input())
print(val)

note = [100,50,20,10,5,2,1,]

for i in note:
    quotient = int(val/i)
    print(f'{quotient} nota(s) de R$ {i},00')
    reminder = val%i
    val = reminder