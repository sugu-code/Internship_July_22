class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_counter = {}
        
        heap = []
        
        for n in arr:
            n_bin = bin(n)[2:]            
            bit_count = n_bin.count('1')            
            heapq.heappush(heap, (bit_count, n))

        results = []
        for _ in range(len(heap)):
            results.append(heapq.heappop(heap)[1])
                
        return results