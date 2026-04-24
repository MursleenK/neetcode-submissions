class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        for num in numbers:
            diff=target-num
            if diff in numbers and diff != num and numbers.index(num)+1 not in ans:
                ans.append(numbers.index(num)+1)
                ans.append(numbers.index(diff)+1)

        return ans

                