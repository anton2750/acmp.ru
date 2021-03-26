a, b = input().split()
bulls = 0
cows = 0
bulls_list = []


for i in range(len(a)):
    if a[i] == b[i]:
        bulls += 1
        bulls_list.append(a[i])
    if a[i] in b and not a[i] in bulls_list:
        cows += 1

print(bulls, cows)

# comment