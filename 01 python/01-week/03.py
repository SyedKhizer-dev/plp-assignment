# (a)

n = 0
a = 0
b = 1
dict1 = {}
while n < 15 and a < 1000:
    if a < 10:
        print(a, "Small")
        dict1[a] = "Small"
    elif a <= 100:
        print(a, "Medium")
        dict1[a] = "Medium"
    else:
        print(a, "Large")
        dict1[a] = "Large"
    a, b = b, a + b
    n += 1
print(dict1)

# (c)
num = 7
for i in range(1, 6):
    print(f"{num}X{i}={num*i}")

# (d)
# [4, 16]
# 7 4 1 -2
