n = int(input())
l = list(map(int, input(). split()))

for el in l:
    if l.count(el) == 1:
        print(el, end = " ")
