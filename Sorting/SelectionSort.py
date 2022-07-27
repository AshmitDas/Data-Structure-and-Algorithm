def selecton_sort(my_list):
    """Big o: O(n^2)"""
    # Loops thorugh the whole list and starts with zero Index 
    # checks except current_index(i.e zeroth) if there is are/is any smaller element 
    # if so it swaps place with smallest element among the smaller elements and 
    # current_index value incremented by 1(i.e zero become 1).
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print(selecton_sort([4,2,6,5,1,3]))