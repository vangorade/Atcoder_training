n, m, c = map(int, input().rstrip("\n").split())
b_list = list(map(int, input().rstrip("\n").split()))
counter = 0
for i in range(n):
    a_list = list(map(int, input().rstrip("\n").split()))
    total = 0
    for i in range(m):
        total += a_list[i] * b_list[i]
    if total + c > 0:
        counter += 1
print(counter)