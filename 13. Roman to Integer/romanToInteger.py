class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000  
    }
        newS = 0
        if 'IV' in s or 'IX' in s:
            s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        if 'XL' in s or 'XC' in s:
            s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        if 'CD' in s or 'CM' in s:
            s = s.replace('CD', 'CCCC').replace('CM','DCCCC')
        for letter in s:
            newS += data[letter]
    
        return newS