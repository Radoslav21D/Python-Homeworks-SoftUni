# list_as_ints = list(map(int, input().split(", ")))
# group = 10
# while list_as_ints:
#     list_as_ints = [num for num in list_as_ints if num <= group]
#     for el in list_as_ints:
#         list_as_ints.remove(el)
#     print(f"Group of {group}'s:{list_to_print}")
#     group += 10

# list_of_numbers = list(map(int, input().split(", ")))
# group_of_numbers = 10
# while list_of_numbers:
#     list_of_numbers = [num for num in list_of_numbers if num <= group_of_numbers]
#     for el in list_of_numbers:
#         list_of_numbers.remove(el)
#     print(f"Group of {group_of_numbers}'s:{list_of_numbers}")
# #  Increase the boundary by 10
#     group_of_numbers += 10


numbers = input().split(", ")
nums = list(map(lambda x: int(x), numbers))
result_list = []
for i in range(10, 100000, 10):
    if len(nums) == 0:
        break
    result_list = [y for y in nums if y <= i]
    nums = [x for x in nums if x > i]
    print(f"Group of {i}'s: {result_list}")
    result_list.clear()
