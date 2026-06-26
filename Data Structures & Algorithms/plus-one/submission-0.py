class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = ""
        for i in range(len(digits)):
            val += str(digits[i])   
        val_num = int(val)          
        val_num += 1                
        result = [int(d) for d in str(val_num)]  
        return result