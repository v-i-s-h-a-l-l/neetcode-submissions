class Solution:
    def reverse(self, x: int) -> int:
        reversed_num=0
        n=abs(x)
        sign = -1 if x < 0 else 1

        while n>0:
            digit=n%10
            reversed_num=reversed_num*10+digit
            n=n//10
       
  
        if reversed_num>2**31-1:
            return 0
        else:
            return sign*reversed_num
        