class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        i, j = 0, len(num) -1
        
        while i<=j:
            
            if num[i] == num[j]:
                if num[i] == '8' or num[i] == '0' or num[i] == '1':
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
            elif num[i] == '6' and num[j] == '9':
                i += 1
                j -= 1
            elif num[i] == '9' and num[j] == '6':
                i += 1
                j -= 1

            else:
                return False
        
        return True
