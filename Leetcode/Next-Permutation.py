class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If found, find the next larger element to swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the tail part
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
