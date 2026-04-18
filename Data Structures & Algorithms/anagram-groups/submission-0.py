class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        seen=[]
        for i in range(len(strs)):
            if strs[i] not in seen:
                compo = [strs[i]]
                seen.append(strs[i])
                for j in range(i+1, len(strs)):
                    if sorted(list(strs[j])) == sorted(list(strs[i])):
                        compo.append(strs[j])
                        seen.append(strs[j])
                ans.append(compo)
        return ans

            