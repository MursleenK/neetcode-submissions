import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        n_l = len(nums)
        for num in nums:
            before = math.prod(nums[:nums.index(num)])
            after = math.prod(nums[nums.index(num)+1:])
            ans.append(before*after)

        return ans
        