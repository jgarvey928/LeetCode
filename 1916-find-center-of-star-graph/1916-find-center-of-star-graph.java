class Solution {
    public int findCenter(int[][] edges) {
        int value1 = edges[0][0];
        int value2 = edges[0][1];
        if(value1 == edges[1][0]){
            return value1;
        }
        if(value1 == edges[1][1]){
            return value1;
        }
        return value2;
    }
}