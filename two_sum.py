def twoSum(nums,target):
    for i in range (len(nums)-1):
        for j in range (i + 1, len(nums)):
            if nums[i] +  nums[j] == target:
                return ([i, j])
            
n = [2,4,6,8, 10, 12, 14]
return_val = twoSum(n, 10)
print(return_val)