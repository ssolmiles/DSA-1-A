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


if __name__ == "__main__":
    
    run_two_sum_demo()
    