x = int(input())

minn1 = 999999999999999999999999999999999999999999999999999
minn2 = 999999999999999999999999999999999999999999999999999

for i in range(x):
    z = int(input())

    if minn1 > z:
        minn1 = z

    if minn2 > z > minn1:
        minn2 = z

print(minn1, minn2)
