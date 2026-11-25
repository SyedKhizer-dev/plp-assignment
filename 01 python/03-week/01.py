# (a)


def fibonacci_gen():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


gen = fibonacci_gen()
# for i in range(10):
#     print(next(gen))

# (b)

result = []


def take(n, gen) -> list:
    while n > 0:
        result.append(next(gen))
        n -= 1
    return result


print(take(10, gen))


# (c)
def squares_gen(limit):
    num = 0

    while limit >= num:
        yield num * num
        num += 1


gen = squares_gen(6)
print(list(gen))
