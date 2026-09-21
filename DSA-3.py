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


def find_jumbled_words(target):
    words = ["listen", "silent", "enlist", "inlets", "google", "glooge"]
    jumbled_words = []
    for word in words:
        if sorted(word) == sorted(target):
            jumbled_words.append(word)
    return jumbled_words
print(find_jumbled_words("listen"))


#insert new work here 

# Naive method to find a pair in a list with the given sum
def findPair(nums, target):
 
    # consider each element except the last
    for i in range(len(nums) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):
 
            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    # No pair with the given sum exists in the list
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)


    # subarrays functions 
    # multidimensional array
    #sorting 
    #basics big o manual computation
