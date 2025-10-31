x = int(input())

maxx = -9999999999999999999999999999999999999999
minn = 9999999999999999999999999999999999999999

for i in range(x):
    z = int(input())
    
    if maxx < z:
        maxx = z

    if minn > z:
        minn = z

print(minn, maxx)
