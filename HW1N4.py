k, l, m, n = map(int, input(). split())

if not(1 <= k <= 8 and 1 <= l <= 8 and 1 <= m <= 8 and 1 <= n <= 8):
    print("Ошибка:диапазон всех координат от 1 до 8")
    
else:
    gorizont = (l == n)
    vert= (k == m)
    diagonal = (abs(m - k) == abs(n - l))

    if vert or gorizont or diagonal:
        print("Да")

    else:
        print("Нет")
