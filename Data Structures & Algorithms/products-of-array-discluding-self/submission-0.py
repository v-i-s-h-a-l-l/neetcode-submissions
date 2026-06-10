class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans1=[]
        for i in range(len(nums)):
            val=1
            for j in range(len(nums)):
                if i!=j:
                    val*=nums[j]
            ans1.append(val)
        return ans1

        