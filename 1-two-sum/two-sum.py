class Solution:
    
 
    def twoSum(self, lst, target):
        seen = set()
        idx = []
        for i in range(len(lst)):
            complement = target - lst[i]
            if complement in seen:
                idx.append(i)
                idx.append(lst.index(complement))
            seen.add(lst[i])
        return idx





