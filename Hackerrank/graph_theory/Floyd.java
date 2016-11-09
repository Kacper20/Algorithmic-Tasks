import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Solution {

    public static class Graph {
        private int verticesCount;
        private int matrix[][];
        public Graph(int verticesCount) {
            this.verticesCount = verticesCount;
            matrix = new int[verticesCount + 1][verticesCount + 1];
            for (int i = 0; i <= verticesCount; i++) {
                for (int j = 0; j <= verticesCount; j++) {
                    matrix[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        public void addEdge(int i, int j, int weight) {
            matrix[i][j] = weight;
        }

        public void computeFloyd() {
            for (int k = 1; k <= verticesCount; k++) {
                for (int i = 1; i <= verticesCount; i++) {
                    for (int j = 1; j <= verticesCount; j++) {
                        int through_k = matrix[i][k] + matrix[k][j] < 0 ? Integer.MAX_VALUE : matrix[i][k] + matrix[k][j];
                        matrix[i][j] = Integer.min(through_k, matrix[i][j]);
                    }
                }
            }
        }

        public int query(int i, int j) {
            if (i == j) return 0;
            return matrix[i][j] == Integer.MAX_VALUE ? -1 : matrix[i][j];
        }
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int nodes = in.nextInt();
        int edges = in.nextInt();
        Graph graph = new Graph(nodes);

        for (int i = 0; i < edges; i++) {
            int from = in.nextInt();
            int to = in.nextInt();
            int weight = in.nextInt();
            graph.addEdge(from, to, weight);
        }
        graph.computeFloyd();
        int queriesCount = in.nextInt();
        for (int i = 0; i < queriesCount; i++) {
            int from = in.nextInt();
            int to = in.nextInt();
            System.out.println(graph.query(from, to));
        }
    }
}