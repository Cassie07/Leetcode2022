class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        res = []
        
        for a in asteroids:
            while res and a < 0 < res[-1]:
                if res[-1] + a > 0:
                    break
                elif res[-1] + a == 0:
                    res.pop()
                    break
                else:
                    res.pop()
            else:
                res.append(a)
        
        return res
