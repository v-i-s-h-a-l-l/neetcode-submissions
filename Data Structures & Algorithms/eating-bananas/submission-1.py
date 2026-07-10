class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            summ=0

            for i in range (len(piles)):
                summ+=math.ceil(piles[i]/k)
            if summ<=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res

        