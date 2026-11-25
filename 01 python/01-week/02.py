scores = [85, 92, 78, 92, 88, 78, 95, 88, 70, 92]

# (a)
unique_scores = set(scores)
print("Unique Scores are:\n", unique_scores)

# (b)
dict1 = {}
for i in unique_scores:
    dict1[i] = scores.count(i)

print("Frequency of scores:\n", dict1)

# (c)
print("Sorted scores: ", sorted(dict1.keys()))

# (d)
min_value = min(scores)
max_value = max(scores)
count_value = len(scores)

tuple_a = (min_value, max_value, count_value)
print("Min, Max, Size of list: ", tuple_a)

# (e)
# [(2,1), (4,2), (7,2), (9,1)]
