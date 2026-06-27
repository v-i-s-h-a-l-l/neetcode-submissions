class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=[]
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    arr.append(i+1)
                    arr.append(j+1)
        return arr
        