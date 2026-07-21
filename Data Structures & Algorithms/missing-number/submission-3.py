class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx=len(nums)
        ans=0
        for i in range(maxx+1):
            if i not in nums:
                ans=i
        return ans
        