class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer: str = ""
        # Loop through first string in list
        for i in range(len(strs[0])):
            # Loop through all strings in list
            for s in strs:
                # Check to make sure we dont go out of bounds
                # if the first word is longer than another word
                # Check if the character in the string is the same
                # as the character in the first string
                if i == len(s) or s[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer