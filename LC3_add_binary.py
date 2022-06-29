class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = list(a)
        b = list(b)

        carry = 0

        # make the lists the same size
        for i in range(0, 100):
            if len(a) < len(b):
                a.insert(0, 0)
            elif len(b) < len(a):
                b.insert(0, 0)
            else:
                break

        m = len(a)
        out_binary = [0]*(m+1)

        #loop through each index from LSB to MSB 
        for i in range (1, m+1):
            if int(a[-i])+int(b[-i])+carry == 0:
                carry = 0
                out_binary[-i] = 0
            elif int(a[-i])+int(b[-i])+carry == 1:
                carry = 0
                out_binary[-i] = 1
            elif int(a[-i])+int(b[-i])+carry == 2:
                carry = 1
                out_binary[-i] = 0
            elif int(a[-i])+int(b[-i])+carry == 3:
                carry = 1
                out_binary[-i] = 1  
        if carry == 0:
            out_binary.pop(0)
        elif carry == 1:
            out_binary[0] = 1
        out_bin_str = ""
        for i in range (0, len(out_binary)):
            out_bin_str += str(out_binary[i])
        return(out_bin_str)

print(Solution().addBinary(a = "1010", b = "1011")) 