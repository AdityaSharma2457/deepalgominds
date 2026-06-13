class Solution:
    def countBitsFlip(self, a, b):
            xor=a^b
            return xor.bit_count()
