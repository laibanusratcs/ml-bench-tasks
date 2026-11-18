
def find_unique_values(numbers):
    unique_values = set(numbers)
    return unique_values


def find_union(set1, set2):
    union_result = set1.union(set2)
    return union_result


def find_intersection(set1, set2):
    intersection_result = set1.intersection(set2)
    return intersection_result


numbers = [1, 2, 2, 3, 4, 4, 5, 5]

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Unique values:", find_unique_values(numbers))
print("Union:", find_union(set1, set2))
print("Intersection:", find_intersection(set1, set2))

# unique_values
# numbers = [1, 2, 2, 3, 4, 4, 5, 5]

# unique_values = set(numbers)

# print(unique_values)

# union and intersection
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# union_result = set1.union(set2)

# this is the testing commit line.


# print(union_result)
# intersection_result = set1.intersection(set2)

# print(intersection_result)