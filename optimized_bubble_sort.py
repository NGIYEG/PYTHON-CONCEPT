def bubble_sort(lst):
    # initialize a variable as False
    # to indicate that no swaps have taken place
    for i in range(len(lst) - 1):
        flag = False

        for j in range(len(lst) - i - 1):
            # to sort in descending order
            # check if item less than next item
            if lst[j] < lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
                # if any element is swapped, 
                # set swapped to True.
                flag = True    

        if not flag:
            break

    return lst

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)
