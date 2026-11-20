
def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None

    return second_largest


def reverse_list(numbers):
    return numbers[::-1]


def remove_duplicates(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique


def find_common_elements(list1, list2):
    common = []

    for num in list1:
        if num in list2 and num not in common:
            common.append(num)

    return common

numbers = [10, 45, 20, 90, 35]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print("Largest number:", find_largest(numbers))
print("Second largest number:", find_second_largest(numbers))
print("Reversed list:", reverse_list([1, 2, 3, 4, 5]))
print("List without duplicates:", remove_duplicates([1, 2, 3, 2, 4, 1, 5]))
print("Common elements:", find_common_elements(list1, list2))

# Largest number
# numbers = [10,20,70,90,220]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest number:", largest)

# Second largest number
# numbers = [10, 45, 20, 90, 35]

# largest = float('-inf')
# second_largest = float('-inf')

# for num in numbers:

#     if num > largest:
#         second_largest = largest
#         largest = num

#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Second largest number:", second_largest)

# reversed_list
# numbers = [1, 2, 3, 4, 5]
# print(numbers[::-1])

# # reversed_list = []

# # for i in range(len(numbers) - 1, -1, -1):
# #     reversed_list.append(numbers[i])

# # print(reversed_list)

# remove_duplicates
# numbers = [1, 2, 3, 2, 4, 1, 5]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print(unique)

# common_elements
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for num in list1:
#     if num in list2 and num not in common:
#         common.append(num)

# print("Common elements:", common)
