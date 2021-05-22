sets = []
 
for i in range(0,3):
    x = input()
    sets.append(x.split())
 
num = int(input())
    
values = []
for i in range(num):
    value = input()
    values.append(value)
 
 
if sets[0][0] in values and sets[0][1] in values and sets[0][2] in values:
    print('Yes')
elif sets[1][0] in values and sets[1][1] in values and sets[1][2] in values:
    print('Yes')
elif sets[2][0] in values and sets[2][1] in values and sets[2][2] in values:
    print('Yes')
elif sets[0][0] in values and sets[1][0] in values and sets[2][0] in values:
    print('Yes')
elif sets[0][1] in values and sets[1][1] in values and sets[2][1] in values:
    print('Yes')
elif sets[0][2] in values and sets[1][2] in values and sets[2][2] in values:
    print('Yes')
elif sets[0][0] in values and sets[1][1] in values and sets[2][2] in values:
    print('Yes')
elif sets[0][2] in values and sets[1][1] in values and sets[2][0] in values:
    print('Yes')
else:
    print('No')