# input : N, a, b eg 7 5 1
# for x in range N
    # if x % n == b % n:
        # print(YES)
# 38 ≡ 23 mod 15 because 38 = 15*2 + 8 and 23 = 15 +8;
n,a,b = map(int, input().split())
for i in range(a):
    if (n*i - b) % a == 0:
        print("YES")
        exit()
print("NO")

# (7 * 1 - 1) % 1 
# (7 * 2 - 1) % 2
# (7 * 3 - 1) % 3
# (7 * 4 - 1) % 4
# (7 * 5 - 1) % 5

# sol2
# A, B, C = map(int, input().split())
# judge = False
# for x in range(1, 102):
#     if (x*A) % B == C:
#         judge = True
# if judge:
#     print("YES")
# else:
#     print("NO")