text = [5, {6.9}, True, 0, None, 'hello', 1.e05, "56"]
str_oka = [i for i in text if type(i) == str]
print(str_oka)
