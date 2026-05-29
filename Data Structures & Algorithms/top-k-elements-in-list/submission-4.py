class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        n = 0
        for _ in nums:
            n += 1
        
        buckets = [[] for _ in range(n + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []
        res_count = 0

        for i in range(n, 0 , -1):
            for num in buckets[i]:
                res.append(num)
                res_count += 1

                if res_count == k:
                    return res

        return res
