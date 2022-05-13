class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        i,j = 0, 0
        res = []
        while i < len(encoded1) and j < len(encoded2):
            
            num1, freq1 = encoded1[i]
            num2, freq2 = encoded2[j]
            
            
            product = num1*num2
            freq = min(freq1, freq2)
            
            
            if freq1 < freq2:
                i += 1
                encoded2[j][1] -= freq
            elif freq1 > freq2:
                j += 1
                encoded1[i][1] -= freq
            else:
                i += 1
                j += 1
                
            if not res or res[-1][0] != product:
                res.append([product, freq])
            else:
                res[-1][1] += freq
        return res
