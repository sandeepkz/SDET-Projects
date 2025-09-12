# Find the Intersection of Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set2 = set(list2)    # O(m)
output = []

for num in list1:    # O(n)
    if num in set2:  # O(1) lookup
        output.append(num)

print(output)  # [4, 5]
