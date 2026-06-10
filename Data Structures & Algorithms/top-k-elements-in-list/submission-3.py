class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        ans1=[]
        cnt=Counter(nums)
        ans1=list(cnt.items())
        ans1.sort(key=lambda x: x[1],reverse=True)
        for i in range(k):
            ans.append(ans1[i][0])


        
        return ans

    

        