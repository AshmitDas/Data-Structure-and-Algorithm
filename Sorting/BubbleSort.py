def bubble_sort(my_list):
    """Big O: O(n^2)"""
    # Loops from 0 to i'th element and if j'th element is greater than j+1'th element, it swaps places with one another.
    
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


print(bubble_sort([4,2,6,5,1,3]))