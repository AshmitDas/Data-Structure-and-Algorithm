def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    """Big O : O(n)"""
    # Assigning pivot_index to the first element of the list and swapping it with the greatest of all the smallest
    # element than the pivot_index element and then returing the pivot_index value.
    swap_index = pivot_index
    
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)

    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    """Big O : O(log n)"""
    # this method breaks the list into left and right in position to the pivot_index.
    # this method will keep on calling itself until there is a single element left in the list.
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

def quick_sort(my_list):
    """Big O : O(n log n)"""
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


# my_list = [4,6,1,7,3,2,5]

# print(pivot(my_list, 0, 6))

print(quick_sort([4,6,1,7,3,2,5]))