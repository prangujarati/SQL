class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dict_operations = {"X++" : 1, "++X" : 1 , "X--" : -1, "--X" : -1}
        f_val = 0
        for i in operations:
            if i in dict_operations:
                f_val = f_val + dict_operations.get(i)
        return f_val


        