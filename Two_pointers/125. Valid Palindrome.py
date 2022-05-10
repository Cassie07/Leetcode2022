class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = [i for i in s if i.isalpha() or i.isdigit()]
        s = ''.join(s)
        i, j = 0, len(s) -1
            
        while i<=j:
            
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
          
        return True
