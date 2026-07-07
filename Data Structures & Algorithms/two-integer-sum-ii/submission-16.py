class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        l = 0
        lv = numbers[l]
        r = len(numbers)-1
        rv = numbers[r]
        while r>l: 
            # if rv+lv == target:
            if numbers[r] + numbers[l] == target:
                # print(1, rv, lv, rv+lv)
                ans.append(l+1)
                ans.append(r+1)
                break
            elif numbers[r] + numbers[l] > target:
                # print("before2:-", r, l, rv, lv, rv+lv)
                r = r-1
                # print("after2:-", r, l, rv, lv, rv+lv)

            elif numbers[r] + numbers[l] < target:
                # print("before3:-", r, l, rv, lv, rv+lv)
                l = l+1
                # print("after3:-", r, l, rv, lv, rv+lv)

            else:
                return "from loop"
        return ans