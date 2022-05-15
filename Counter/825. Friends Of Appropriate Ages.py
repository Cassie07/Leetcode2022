class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
 
        
        def request(x,y):
            if y <= 0.5*x +7 or y > x or (y > 100 and x < 100):
                return False
            return True
        
        count = 0

        ages_map = collections.Counter(ages)
        ages = list(ages_map.keys())
        ages.sort(reverse=True)


        for i in range(len(ages)):
            for j in range(i+1,len(ages)):

                if request(ages[i],ages[j]):
                    count += ages_map[ages[i]]* ages_map[ages[j]]
                   
            if request(ages[i],ages[i]):
                count += ages_map[ages[i]]*(ages_map[ages[i]]-1)

        return count
        
