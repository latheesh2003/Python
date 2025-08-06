def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

my_list = [4, 2, 8, 1, 9, 0, -1]

# Full bubble sort
for i in range(0, len(my_list)):
    for j in range(0, len(my_list) - 1):
        if my_list[j] > my_list[j + 1]:
            swap(my_list, j, j + 1)

print(my_list)
