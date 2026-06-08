# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return pairs

        result = [pairs[:]]
        n = len(pairs)
        for i in range(1,n):
            key_pair = pairs[i]
            key = pairs[i].key
            j = i - 1
            while j >= 0 and key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = key_pair
        
            result.append(pairs[:])


        return result