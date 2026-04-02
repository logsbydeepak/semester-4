data = {"a": 50, "b": 20, "c": 40, "d": 10}
ascending = dict(sorted(data.items(), key=lambda item: item[1]))
descending = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

print("Original dictionary:", data)
print("Ascending order by values:", ascending)
print("Descending order by values:", descending)

"""
Original dictionary: {'a': 50, 'b': 20, 'c': 40, 'd': 10}
Ascending order by values: {'d': 10, 'b': 20, 'c': 40, 'a': 50}
Descending order by values: {'a': 50, 'c': 40, 'b': 20, 'd': 10}
"""
