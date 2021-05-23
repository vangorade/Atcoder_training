n = int(input())
arr = sorted(list(map(int, input().split())),reverse=True)

alice, bob = 0, 0

for i in range(n):
    if(i % 2 == 0):
        alice += arr[i]
    else:
        bob += arr[i]
print(alice - bob)

