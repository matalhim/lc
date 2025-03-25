class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            diff_i = heights[i+1] - heights[i]

            if diff_i > 0:
                heapq.heappush(heap, diff_i)
                if len(heap) > ladders:
                    min_diff = heapq.heappop(heap)
                    bricks -= min_diff
                    if bricks < 0:
                        return i

        return len(heights) - 1

        