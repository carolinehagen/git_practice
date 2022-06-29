class Solution:
    def hammingWeight(self, n: int) -> int:
        # convert the integer to a list 
        count = []*32
        counter = 0
        for i in range(0, 32):
            if n%10 == 1:
                counter += 1
            n = int(n/10)
            print(n)

        return counter 
#jk just convert the int to a list and then count the ones. (use .count())
        
print(Solution().hammingWeight(n = 1011))