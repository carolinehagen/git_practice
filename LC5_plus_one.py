class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        
        #append each number to a string
        numbers_string = " "
        for i in range(0, len(digits)):
            numbers_string += str(digits[i])

        

        #turn the string into an int 
        numbers_int = int(numbers_string)
        
        #add one to the int 
        numbers_plus_one = numbers_int +1
        #use modulus to turn each number back into a list 
        list_numbers = [int(i) for i in str(numbers_plus_one)]
        return list_numbers


print(Solution().plusOne(digits = [1, 2, 3, 4]))