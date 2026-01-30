# data_op.py

data = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Remove duplicates
unique_data = list(set(data))
print("Unique:", unique_data)

# Sort
sorted_data = sorted(unique_data)
print("Sorted:", sorted_data)

# Max, min, average
print("Max:", max(data))
print("Min:", min(data))
print("Average:", sum(data)/len(data))

# Dictionary comprehension example
squares = {x: x**2 for x in data}
print("Squares:", squares)
