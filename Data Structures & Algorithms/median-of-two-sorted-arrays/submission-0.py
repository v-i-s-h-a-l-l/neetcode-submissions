class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsa=nums1+nums2
        median=0
        numsaa=sorted(numsa)
        low=0
        high=len(numsaa)-1
        mid=(low+high)//2
        if len(numsaa)%2!=0:
            median=numsaa[mid]
        elif len(numsaa)%2==0:
            median=(numsaa[mid]+numsaa[mid+1])/2       
        return median 