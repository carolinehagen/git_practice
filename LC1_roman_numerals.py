# define the values 
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

# create a class 
class Solution:
    # create the function
    def roman_conversion(self, s: str) -> int:
        #self.str = str

        # initalize a total 
        total = 0
        # initialize an iterator 
        i = 0
        # make a while loop that loops until the entire s has been interated through 
        while i < len(s):
            # if statement for subtractive case EX IV
            if i + 1 > len(s) and values[s[i+1]] >= values[s[i]]:
                total += values[s[i+1]] - values[s[i]]
                i += 2 
            # if statement is not subtractive
            else: 
                total += values[s[i]]
                i += 1
        return total 
    
print(Solution().roman_conversion(s = "MI"))