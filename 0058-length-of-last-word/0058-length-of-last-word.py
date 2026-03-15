class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = ""
        adv = False
        for char in reversed(s):
            if char != " ":
                adv = True
            if adv == True:
                if char == " " :
                    return len(result)
                result += char
        return len(result)