from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = set()
        for num in nums:
            if num in storage:
                return True
            else:
                storage.add(num)
        return False

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 1]
print(solution.containsDuplicate(nums))
