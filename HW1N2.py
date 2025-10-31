ch = int(input())

x = 1

for x in range(1, ch + 1):

    if ch % x == 0:
        print(x, end = " ")
