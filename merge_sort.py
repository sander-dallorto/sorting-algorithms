def merge_sort(nums):
    nums_length = len(nums)
    median = nums_length // 2

    if nums_length < 2:
        return nums

    first = merge_sort(nums[:median])
    second = merge_sort(nums[median:])

    return merge(first, second)

def merge(first, second):
    final = list()
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1

        else:
            final.append(second[j])
            j += 1

    while i < len(first):
        final.append(first[i])
        i += 1

    while j < len(second):
        final.append(second[j])
        j += 1
        
    return final
    
if __name__ == "__main__":
  
    test_cases = [
        [3, 2, 1],
        [5, 4, 3, 2, 1],
        [4, -7, 1, 0, 5],
        []
    ]
    
    for test in test_cases:
        print(f"Input: {test}")
        result = merge_sort(test)
        print(f"Output: {result}")
        print()


   
