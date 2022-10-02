numbers = [21, 43, 46, 65, 76, 88, 93, 102]
result = sorted(filter(lambda x: x % 2 == 0, numbers)) + sorted(filter(lambda x: x % 2, numbers))
print(result)
