
#init, butt1 is light up, stop when button2 is light up
# basically if 2nd light is get skipped then return -1

n = int(input())
arr = [int(input()) - 1 for _ in range(n)]

light = 0
couter = 0

while(light != 1):
    light = arr[light]
    counter += 1

    if(counter > n): # we skipped second 
        print(-1)
        exit()
print(counter)





