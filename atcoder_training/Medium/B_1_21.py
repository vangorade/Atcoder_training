a, b = input().split()
n = int(a + b)
for i in range(10**3):
    if i*i == n:
        print('Yes')
        exit()
print('No')