class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        for i in range(len(nums)):
            if count[nums[i]]==1:
                return nums[i]
                
  
        