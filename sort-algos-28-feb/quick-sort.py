"""
How quick sort works:
- A pivot is chosen(I.e. mean of three):
    - The first, middle and last elements of the list are identified
    - The identified items are sorted properly and the middle one is estimated to be close to the middle of the list
- An item from the left is chosen, which is the first one that is larger than the pivot
- An item from the right is chosen, whichis the first on that is smaller than the pivot
- Switch these two items that have been selected
- Repeat the process until the item from left has a greater index than the item from the left
- Swap the item from the left with the pivot
- The two separate lists on either side of the pivot are isolated and have the process above perfomed on them recursively



A pivot is an item in the final sorted array that:
- Has a correct position
- All the items to the left are smaller
- All the items to the right are larger
"""

# this is the data set that will be used for the project
p_data = [3, 9, 2, 1, 8, 7, 6, 5, 9, 6, 2, 8]

# checks if the data has an even number of items
if (len(p_data) % 2) == 0:
    # if it does then the middle item is the one right middle one
    middle = p_data[int(len(p_data) / 2)]

# checks if the data does not have an even number
else:
    # if it does then the middle item is the one at the actual middle of the list
    middle = p_data[(len(p_data) // 2)]


quartiles = [p_data[0], middle, p_data[-1]]
quartiles.sort()
p_pivot = quartiles[1]


def quick_sort(data, pivot):
    while True:
        print(data)
        print(pivot)
        # data.remove(pivot)

        for e, i in enumerate(data):
            if i > pivot:
                l_index = e
                break

        for i in range(len(data) - 1, -1, -1):
            if data[i] < pivot:
                r_index = i
                break

        if l_index > r_index:
            break
        else:
            data[e], data[r_index] = data[r_index], data[e]


quick_sort(p_data, p_pivot)
