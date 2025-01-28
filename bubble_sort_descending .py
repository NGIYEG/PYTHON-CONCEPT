# Write a program to sort the list items in descending order using bubble sort.

# Create a function named bubble_sort() that takes a list as its argument.
# Sort the list in descending order within the function and return the sorted list.
# Print the sorted list from outside the function.
# Tip: In this case, you need to swap elements if the current element is smaller than the next element.

def bubble_sort(lst):
    # outer loop to access each element in the list
    for i in range(len(lst)):

        # inner loop to compare list elements
        for j in range(len(lst) - 1):           
            
            # swap if necessary
            if lst[j]<lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

data_list = [int(x) for x in input().split()]


bubble_sort(data_list)
print(data_list)