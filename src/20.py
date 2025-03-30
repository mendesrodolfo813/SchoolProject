def find_max_even_index(nums):
    max_even = 0
    index_of_max_even = -1
    
    for i in range(len(nums)):
        if nums[i] % 2 == 0 and nums[i] > max_even:
            max_even = nums[i]
            index_of_max_even = i

    return max_even, index_of_max_even
