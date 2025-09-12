# Write a Python program to manage a to-do list with the following steps:
"""
1.Start with an empty task list.
2.Add tasks one by one.
3.Add a task at a specific position in the list.
4.Add multiple tasks at once from another list.
5.Remove the last task from the list.
"""

my_list = []
print(my_list)
for i in range(5):
    my_list.append(i)
print(my_list)
my_list.insert(3, 'sk')
print(my_list)
my_list2 = ['a', 'b', 'c', ['xyz']]
my_list.extend(my_list2)
print(my_list)
my_list.pop()
print(my_list)
"""
6.Remove the first task from the list.
7.Delete a specific task by its name.
8.Erase all tasks at once.
9.Find the position of a particular task.
10.Count how many times a given task appears in the list.
"""
my_list.pop(0)
print(my_list)
my_list.remove('a')
print(my_list)
# my_list.clear()
# print(my_list)
print(my_list.index('sk'))
my_list.append('sk')
print(my_list)
print(my_list.count('sk'))
"""
11.Arrange the tasks in alphabetical order.
12.Display the tasks in reverse order.
13.Create a backup of the task list.
14.Show only the first 3 tasks and the last 2 tasks.
15.Create a new list where all tasks are written in UPPERCASE.
"""
items = [x for x in my_list if not isinstance(x, str)]
print(items)
#print(items.sort())
#print(my_list.reverse())
#my_list_copy = my_list.copy()
print('---------')
print(my_list[:3])
print(my_list[-2:])
print('-----')
upper_my_list = []
my_list_l = ['A', 'b', 'c']
for i in my_list_l:
    upper_my_list.append(i.upper())
print(upper_my_list)