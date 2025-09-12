# Move all zeros to the end (while keeping order of non-zeros)

input_list = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
# Output → [1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0, 0]
list1 = []
counter = 0

for num in input_list:
    if num != 0:
        list1.append(num)
    else:
        counter += 1

for i in range(counter):
    list1.append(0)

