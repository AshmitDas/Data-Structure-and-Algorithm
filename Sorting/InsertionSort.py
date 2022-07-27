def insertion_sort(my_list):
    """Big O: O(n^2)"""
    # checks current index value with previous index and if it's value smaller 
    # than previous index , it swaps places and current index incremented by 1.
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([4,2,6,5,1,3]))