n = int(input())
l = list(map(int, input(). split()))

max = l[0]
min = l[0]
max_index = 0
min_index = 0

for i in range(n):
    if max < l[i]:
        max = l[i]
        max_index = i
    if min > l[i]:
        min = l[i]
        min_index = i

l[max_index], l[min_index] = l[min_index], l[max_index]

print(*l)
