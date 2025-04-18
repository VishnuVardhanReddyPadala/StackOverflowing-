class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Update closest sum if the current sum is closer to the target
                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # Exact match found

        return closest_sum
