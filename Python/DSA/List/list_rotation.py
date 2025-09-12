# Rotate a List by k Positions

input_list = [1, 2, 3, 4, 5]
k = 3
l = len(input_list)
k = k % l
# Output → [4, 5, 1, 2, 3]

input_list.reverse()
input_list[:k] = reversed(input_list[:k])
input_list[k:] = reversed(input_list[k:])
print(input_list)
