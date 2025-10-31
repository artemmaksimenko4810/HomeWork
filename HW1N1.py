l, r = map(int, input(). split())

x = 1

while x < l:
    x = x * 2

print(x)

while x < r:
    x = x * 2

    if x > r:
        break

    print(x)
