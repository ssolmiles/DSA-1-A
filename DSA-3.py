def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) 
        guess = list[mid]
        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  
print(binary_search(my_list, -1))



def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))



def find_irrelevant(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return
