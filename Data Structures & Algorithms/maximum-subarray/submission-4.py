class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=nums[0]
        summ=nums[0]
        for i in range(1,len(nums)):
            summ=max(nums[i],summ+nums[i])
            maxx=max(maxx,summ)
        return maxx             
        