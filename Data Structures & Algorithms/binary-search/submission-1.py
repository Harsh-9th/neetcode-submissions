class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt = 0
        rt = len(nums) - 1

        while lt <= rt and target >= nums[lt] and target <= nums[rt]:
            if lt == rt:
                if target == nums[lt]:
                    return lt
                return -1

            estim = lt + int(((rt - lt)/(nums[rt] - nums[lt])) * (target - nums[lt]))

            if nums[estim] == target:
                return estim
            elif nums[estim] < target:
                lt = estim + 1
            else:
                rt = estim - 1
        return -1