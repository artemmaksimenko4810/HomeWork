n = int(input())
l = list(map(int, input(). split()))

max1 = max2 = float("-inf")
min1 = min2 = float("inf")

for i in l:
    if max1 < i:
        max2 = max1
        max1 = i

    elif i > max2:
        max2 = i

    if min1 > i:
        min2 = min1
        min1 = i

    elif min2 > i:
        min2 = i

product_max = max1 * max2
product_min = min1 * min2

if product_max > product_min:
    print(max1, max2)

elif product_min > product_max:
    print(min1, min2)

else:
    if max1 != min1:
        print(max1, max2, min1, min2)

    else:
        print(max1, max2)
