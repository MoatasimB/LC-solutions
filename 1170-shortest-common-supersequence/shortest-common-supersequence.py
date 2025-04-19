class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        prev_row = [str2[:i] for i in range(len(str2) + 1)]

        for i in range(1, len(str1) + 1):
            curr_row = [str1[:i]] + [None for _ in range(len(str2))]
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    curr_row[j] = prev_row[j - 1] + str1[i-1]
                else:
                    if len(curr_row[j - 1]) < len(prev_row[j]):
                        curr_row[j] = curr_row[j - 1] + str2[j - 1]
                    else:
                        curr_row[j] = prev_row[j] + str1[i - 1]
            prev_row = curr_row
        
        return prev_row[len(str2)]