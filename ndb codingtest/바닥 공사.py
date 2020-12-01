n = int(input())
total = [1,3]
for _ in range(n-2):
    total.append(total[-1]+total[-2]*2)
print(total)