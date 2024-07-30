def removeduplicates(nums):
    if not nums:
        return 0
    
    k=1
    for i in range(1,len(nums)):
        if nums[i] != nums[k-1]:
            nums[k]=nums[i]
            k=k+1

    return k
    
nums =[1,1,2,2,3,4,5,5]

k= removeduplicates(nums)

print(f"The number of unique elements is: {k}")
print(f"Array after removing duplicates: {nums[:k]}")

    