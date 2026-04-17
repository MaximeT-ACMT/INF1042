import random

numbers_list = [random.randint(1, 20) for _ in range(100)]

unique_numbers_set = set(numbers_list)

final_list = sorted(list(unique_numbers_set))

print("Original list:", len(numbers_list))
print("New list:", final_list)