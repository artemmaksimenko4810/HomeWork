k = int(input())

h = k // 3600
ost = k % 3600
m = ost // 60

print(f"{h} hours {m} minutes")
