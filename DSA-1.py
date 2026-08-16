# BASIC DSA CODING EXAMPLES
# including its breakdown and explanation of how it works.
# Basic DSA manipulation starting from graphs [Discrete Mathematics] to sorting algorithms and searching algorithms.
#08-16-2026
# Last Topic: Graph and Sets [1st year, 2nd semester]
# Recent: 2nd year, 1st Semester DSA Continuation.


# Problem: Given a list of numbers and a target, return the INDICES of
# the two numbers that add up to the target.
#
# Example: nums = [2, 7, 11, 15], target = 9  ->  return [0, 1]
#          because nums[0] + nums[1] == 2 + 7 == 9
#
# The naive way is to check every pair (two nested loops = O(n^2)).
# The clever way uses a hash map (a Python dict) to remember numbers
# we've already seen, so we can find the answer in a SINGLE pass = O(n).
#
# How it works:
#   - Walk through the list one number at a time.
#   - For each number, calculate "what number would I need to pair with
#     this one to reach the target?" -> that's called the "complement".
#   - Check if we've already seen that complement before. If yes, done!
#   - If not, store the CURRENT number (and its index) in the dict,
#     in case a LATER number needs to pair with it.

def two_sum(nums, target):
    seen = {}  # maps: number -> index where we saw it

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index

    return []  # no pair found


def run_two_sum_demo():
    print("=== PART 1: Two Sum (Hash Map) ===")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("Array:", nums, "| Target:", target)
    print("Indices that add up to target:", result)
    print(f"Check: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")
    print()


#ROTATE ARRAY IN PLACE

# Problem: Rotate an array to the RIGHT by k steps, using the SAME
# array (no creating a brand new list to cheat).
#
# Example: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
#          -> [5, 6, 7, 1, 2, 3, 4]
#
# The trick: rotating right by k is the same as:
#   1. Reverse the WHOLE array
#   2. Reverse the FIRST k elements
#   3. Reverse the REMAINING elements
#
# Example walkthrough with [1,2,3,4,5,6,7], k=3:
#   Step 1 (reverse all):        [7,6,5,4,3,2,1]
#   Step 2 (reverse first 3):    [5,6,7,4,3,2,1]
#   Step 3 (reverse the rest):   [5,6,7,1,2,3,4]  <- done!

def reverse_section(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # in case k is bigger than the 

    reverse_section(nums, 0, n - 1)     # reverse whole array
    reverse_section(nums, 0, k - 1)     # reverse first k elements
    reverse_section(nums, k, n - 1)     # reverse the rest

    return nums


def run_rotate_array_demo():
    print("=== PART 2: Rotate Array In-Place ===")
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Before:", nums, "| Rotate right by:", k)
    rotate_array(nums, k)
    print("After: ", nums)
    print()


#BUBBLE SORT

# Problem: Sort an array from smallest to largest, WITHOUT using
# Python's built-in sort()/sorted().
#
# Bubble Sort idea: repeatedly compare NEIGHBORING pairs of elements
# and swap them if they're in the wrong order. After each full pass
# through the array, the largest unsorted number "bubbles up" to its
# correct spot at the end -- like a bubble rising to the top of water.
#
# Example: [5, 1, 4, 2, 8]
#   Pass 1: compare (5,1)->swap, (5,4)->swap, (5,2)->swap, (5,8)->no swap
#           result: [1, 4, 2, 5, 8]   <- 8 is now in its final spot
#   Pass 2: [1, 2, 4, 5, 8]           <- 5 is now in its final spot
#   ...continues until no swaps are needed.

def bubble_sort(nums):
    n = len(nums)

    for pass_num in range(n - 1):
        swapped = False

        for i in range(n - 1 - pass_num):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        if not swapped:   # already sorted, no need to keep looping
            break

    return nums


def run_bubble_sort_demo():
    print("=== PART 3: Bubble Sort ===")
    nums = [5, 1, 4, 2, 8, 0, 3]
    print("Before:", nums)
    bubble_sort(nums)
    print("After: ", nums)
    print()


if __name__ == "__main__":
    
    run_two_sum_demo()
    