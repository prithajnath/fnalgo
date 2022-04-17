from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while True:
                if j >= k or j >= len(nums) or k <= i:
                    break
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    results.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    continue
                if current_sum > 0:
                    k = k - 1
                if current_sum < 0:
                    j = j + 1
        return [[a, b, c] for a, b, c in results]
