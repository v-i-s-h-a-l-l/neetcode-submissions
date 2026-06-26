class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)   # convert to binary, pad to 32 bits
        reversed_binary = binary[::-1]   # reverse the string
        return int(reversed_binary, 2)   # convert back to integer