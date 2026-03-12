class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            # If the character is already in the map and within the current window
            if s[end] in char_map and char_map[s[end]] >= start:
                # Move the start to the position after the last occurrence
                start = char_map[s[end]] + 1
            
            # Update the last seen index of the character
            char_map[s[end]] = end
            # Calculate the window size and update max_length
            max_length = max(max_length, end - start + 1)
            
        return max_length