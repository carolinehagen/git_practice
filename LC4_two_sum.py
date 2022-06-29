class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #loop through each number 
            #loop through each number + 1 
                # if nums[i] + nums[j] == target, return 
        
        for i in range (0, len(nums)):
            for j in range(i +1, len(nums)):
                if nums[i] + nums[j] == target:
                    output = [i, j]
                    return output 
                    
print(Solution().twoSum(nums = [2, 5, 5, 11], target = 10))