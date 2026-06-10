class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        used=set()
        
        for i in range(len(strs)):
            if i in used:
                continue
            group=[strs[i]]
            used.add(i)

            for j in range(i+1,len(strs)):
                if "".join(sorted(strs[i]))=="".join(sorted(strs[j])):
                    group.append(strs[j])
                    used.add(j)
            ans.append(group)
        return ans


        