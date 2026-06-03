class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1 , -1):
            if not carry:
                break
            d = digits[i]
            d = (d + carry) % 10
            digits[i] = d
            
            carry = 1 if d == 0 else 0


        
        
        if carry:
            digits.insert(0, 1)
        
        return digits