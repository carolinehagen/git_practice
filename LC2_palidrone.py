class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x/10 < 1:
            return True 
    
        # obtain the size 
        for i in range(1,100):
            if x < 10**i:
                length = i 
                break     

        # loop that stores each individual number 
        j = [0]*(length+1)
        for i in range(1, length+1):
            j[i] = x%10
            x = int(x/10)
            
        
        # compare the last and first of every number 
        count = 0
        for i in range(1, length +1):
            if j[i] == j[-i]:
                count += 1
        
        if count == length:
            return True
        else:
            return False
            
        
print(Solution().isPalindrome(x = 101101))