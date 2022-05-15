class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        room = []
        
        for interval in sorted(intervals):
            if not room:
                heapq.heappush(room, interval[1])
            else:
                if interval[0] >= room[0]:
                    heapq.heappop(room)
                heapq.heappush(room, interval[1])
                    
        return len(room)
