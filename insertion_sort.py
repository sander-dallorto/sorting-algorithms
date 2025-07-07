def insertion_sort(nums):
    for i in range(0, len(nums)):
        j = i

        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

    return nums

if __name__ == "__main__":
    # Test cases for debugging
    test_cases = [
        [3, 2, 1],
        [5, 4, 3, 2, 1],
        [4, -7, 1, 0, 5],
        []
    ]
    
    for test in test_cases:
        print(f"Input: {test}")
        result = insertion_sort(test)
        print(f"Output: {result}")
        print()
