def quick_sort(nums, low, high):
    if low < high:
        pivot = partition(nums, low, high)
        quick_sort(nums, low, pivot - 1)
        quick_sort(nums, pivot + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    
    return i+1

if __name__ == "__main__":
    import random
    import time

    large_list = [random.randint(0, 100000) for _ in range(10000)] # 10,000 random numbers
    print(f"Original list size: {len(large_list)}")

    
    list_to_sort = large_list[:]

    start_time = time.time()
    quick_sort(list_to_sort, 0, len(list_to_sort) - 1)
    end_time = time.time()

    print(f"Time taken to sort: {end_time - start_time:.4f} seconds")

    print(f"Sorted (first 10): {list_to_sort[:10]}")
    print(f"Sorted (last 10): {list_to_sort[-10:]}")

    is_sorted = all(list_to_sort[i] <= list_to_sort[i+1] for i in range(len(list_to_sort) - 1))
    print(f"Is the list truly sorted? {is_sorted}")
