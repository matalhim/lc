class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        for code in barcodes:
            if code in freq:
                freq[code] += 1
            else:
                freq[code] = 1
                
        heap = []
        for code, count in freq.items():
            heapq.heappush(heap, (-count, code))  
        
        res = []
        while len(heap) >= 2:
            count1, code1 = heapq.heappop(heap)
            count2, code2 = heapq.heappop(heap) 
            res.append(code1)
            res.append(code2)
            if count1 + 1 < 0: 
                heapq.heappush(heap, (count1 + 1, code1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, code2))

        if heap:
            res.append(heap[0][1])
        return res
        