class Solution:
    def search(self, nums: List[int], target: int) -> int:
        val=-1

        for i in range(len(nums)):
            if nums[i]==target:
                val=i
        return val
           
        