#! /usr/bin/env python3
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List:
        output = []
        q = []
        left = right = 0

        while right < len(nums):
            """
            q is a monotonic queue, so the values are
            in decreasing order.
            Only small values can be inserted in the
            queue.
            """
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.pop(0)

            """
            Sliding the window and adding the maximum
            element to the output list.
            """
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1

        return output
