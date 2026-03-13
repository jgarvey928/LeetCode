class Solution {
    public int findCenter(int[][] edges) {
        // In a star graph, the center node must appear in every edge.
        // We only need to compare the two nodes of the first edge 
        // with the nodes of the second edge.
        
        int u1 = edges[0][0];
        int v1 = edges[0][1];
        
        int u2 = edges[1][0];
        int v2 = edges[1][1];
        
        // If u1 is present in the second edge, it is the center.
        // Otherwise, v1 must be the center.
        return (u1 == u2 || u1 == v2) ? u1 : v1;
    }
}