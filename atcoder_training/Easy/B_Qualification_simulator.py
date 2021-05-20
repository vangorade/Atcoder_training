# if the current participant is non-student, he/she does not qualify.

# if the current participant is a Japanese student, he/she qualifies if and only if the value of counter 1 is smaller than A+B.
# If he/she qualifies, we will increment the value of counter 1 by 1.

# if the current participant is an oversea student, he/she qualifies if and only if the value of counter 1 is smaller than A+B and the value of counter 2 is smaller than B. \
# If he/she qualifies, we will increment the values of both counters by 1.

n,a,b = map(int, input().split())
arr = list(input())

oversea = 0
Japanese = 0

for i in range(len(arr)):
    if(arr[i] == 'a' and Japanese < (a+b)):
        print("Yes")
        Japanese += 1
    elif arr[i] == 'b' and Japanese < (a+b) and oversea<b:
        print("Yes")
        Japanese += 1
        oversea += 1
    else:
        print("No")

