# Find the second-largest number in a list without using max() twice.

input_list = [10, 20, 4, 45, 99, 98, 99]

first_highest = second_highest = float('-inf')
for num in input_list:
    if num > first_highest:
        second_highest = first_highest
        first_highest = num
    elif first_highest > num > second_highest:
        second_highest = num

if second_highest == float('-inf'):
    print("No second highest number")
else:
    print(f"Second highest: {second_highest}")
