class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        pd = {'(' : ')', '{' : '}', '[' : ']'}
        for i in s:
            if i in pd.keys():
                lst.append(i)
            elif i in pd.values():
                if (lst and i == pd.get(lst[-1],0)):
                    lst.pop()
                else:
                    lst.append(i)
        if lst :
            return False
        else:
            return True



        