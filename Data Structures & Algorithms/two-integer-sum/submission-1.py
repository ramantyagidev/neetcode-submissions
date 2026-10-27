class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        empty = {}

        for i, num in  enumerate(nums):
            need = target - num

            if need in empty:
                return [empty[need], i]

            empty[num] = i

