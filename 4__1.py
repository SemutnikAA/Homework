n = int(input())
m = int(input())
k = int(input())
i = 0
while i < k:
    if n % m == 0 and n > k:
        print(n)
        i += 1
    n += 1
