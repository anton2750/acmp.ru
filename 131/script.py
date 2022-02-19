a = int(input())

m = 0
f = -1

for level in range(a):
    age, gender = map(int, input().split())
    if gender == 1 and age > m:
        m = age
        f = level + 1

print(f)
