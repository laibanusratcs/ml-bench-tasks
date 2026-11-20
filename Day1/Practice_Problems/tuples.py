def count_occurrences(numbers, target):
    count = 0

    for num in numbers:
        if num == target:
            count += 1

    return count


def tuple_to_list(my_tuple):
    my_list = list(my_tuple)
    return my_list


def list_to_tuple(my_list):
    my_tuple = tuple(my_list)
    return my_tuple


numbers = (1, 2, 3, 2, 4, 2, 5)

my_tuple = (10, 20, 30, 40)

my_list = [10, 20, 30, 40]

print("Occurrences of 2:", count_occurrences(numbers, 2))

print("Tuple converted to list:", tuple_to_list(my_tuple))
print("Type:", type(tuple_to_list(my_tuple)))

print("List converted to tuple:", list_to_tuple(my_list))
print("Type:", type(list_to_tuple(my_list)))

# conversion
# my_tuple = (10, 20, 30, 40)

# my_list = list(my_tuple)

# print(my_list)
# print(type(my_list))


# my_list = [10, 20, 30, 40]

# my_tuple = tuple(my_list)

# print(my_tuple)
# print(type(my_tuple))

# Count Occurence
# numbers = (1, 2, 3, 2, 4, 2, 5)

# count = 0

# for num in numbers:
#     if num == 2:
#         count += 1

# print("Occurrences of 2:", count)