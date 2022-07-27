def merge(list1, list2):
    """Big O: O(n)"""
    # Merges the lists into one until it's similar to the length of the original list and sorts elements while merging

    combined = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1


    # Adds the remaining element of one list when the other list becomes empty.

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(my_list):
    """Big O: O(log n)"""
    #Breaks the list into two halves and continues until each list containes only one element

    if len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2

    left = my_list[:mid]
    right =  my_list[mid:]

    return merge(merge_sort(left), merge_sort(right))


"""Big O: O(n log n)"""
print(merge_sort([5,4,7,1,3,2,8,6]))