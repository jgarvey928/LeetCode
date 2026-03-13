class Solution {
    public String longestCommonPrefix(String[] strs) {
        // If the array is empty, there is no common prefix
        if (strs == null || strs.length == 0) {
            return "";
        }
        
        // Start by assuming the first string is the common prefix
        String prefix = strs[0];
        
        // Compare the prefix with each subsequent string in the array
        for (int i = 1; i < strs.length; i++) {
            // While the current string does not start with the prefix
            while (strs[i].indexOf(prefix) != 0) {
                // Shorten the prefix by 1 character from the end
                prefix = prefix.substring(0, prefix.length() - 1);
                
                // If the prefix becomes empty, there is no common prefix at all
                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }
        
        return prefix;
    }
}