class Solution:
    def romanToInt(self, s: str) -> int:
        # Largest to smallest -> add
        # Smallest to largest -> subtract 
        total = 0
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(len(s)):
            # Check to make sure we are in bounds
            if i + 1 < len(s) and numerals[s[i]] < numerals[s[i +1]]:
                    total -=  numerals[s[i]]
            else:
                total += numerals[s[i]]

        return total
            