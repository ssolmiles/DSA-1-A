import numbers


def get_first(arr):
    return arr[0] 

numbers = [10, 20, 30, 40, 50]
print(get_first(numbers))  # 10
# O(1) constant


def find_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

# O(n) linear
numbers = [3, 7, 2, 9, 4]
print(find_max(numbers))  


def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                return True
    return False

# Quadratic time complexity O(n^2)
numbers = [1, 2, 3, 4, 2]
print(has_duplicates(numbers)) 