class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr1=[]
        
        for i in range(len(temperatures)):
            found=False
            for j in range(i,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    arr1.append(j-i)
                    found=True
                    break
            if not found:
                arr1.append(0)
        return arr1

        