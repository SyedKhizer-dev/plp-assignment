numbers = [3, 7, 12, 19, 24, 31, 40, 47, 56, 63]

sq_list = [x * x for x in numbers if x % 2 == 1]
print("Odd numbers squared: ", sq_list)

div_four = list(filter(lambda x: x % 4 == 0, numbers))
print(div_four)

padded_num = list(map(lambda x: str(x).zfill(3), numbers))
print(padded_num)

dict1 = {x: ("even" if x % 2 == 0 else "odd") for x in numbers}
print(dict1)
