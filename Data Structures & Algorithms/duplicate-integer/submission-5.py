class Solution:
    def merge_sort(self, arr):
        n = len(arr)

        if n > 1:
            mid = n // 2
            lt = arr[:mid]
            rt = arr[mid:]

            self.merge_sort(lt)
            self.merge_sort(rt)

            i = j = k = 0

            while i < len(lt) and j < len(rt):
                if lt[i] < rt[j]:
                    arr[k] = lt[i]
                    i += 1

                else:
                    arr[k] = rt[j]
                    j += 1
                
                k += 1
            
            while i < len(lt):
                arr[k] = lt[i]
                i += 1
                k += 1
            
            while j < len(rt):
                arr[k] = rt[j]
                j += 1
                k += 1

        return arr


    def hasDuplicate(self, nums: List[int]) -> bool:

        nums = self.merge_sort(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False
