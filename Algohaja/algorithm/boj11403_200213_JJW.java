import java.util.ArrayList;
import java.util.Scanner;

public class boj11403_200213_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        String in = null;
        Node[] nodes = new Node[N];
        int[][] paths = new int[N][N];

        for (int i = 0; i < N; i++) {
            nodes[i] = new Node(N);
            nodes[i].at = i;
        }

        for (int i = 0; i < N; i++) {
            in = sc.nextLine();
            for (int j = 0; j < N; j++) {
                if (in.charAt(j * 2) == '1') {
                    nodes[i].childNodes.add(nodes[j]);
                }
            }
        }

        StringBuilder output = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (bfs(nodes, new boolean[N], paths, i, j)) {
                    paths[i][j] = 1;
                    output.append("1 ");
                } else {
                    output.append("0 ");
                }
            }
            output.append("\n");
        }

        System.out.println(output);
    }

    public static boolean bfs(Node[] nodes, boolean[] isVisited, int[][] paths, int now, int end) {
        Node childNode = null;
        isVisited[nodes[now].at] = true;
        for (int i = 0; i < nodes[now].childNodes.size(); i++) {
            childNode = nodes[now].childNodes.get(i);
            if (paths[childNode.at][end] == 1 || childNode.at == end) {
                return true;
            }
        }

        for (int i = 0; i < nodes[now].childNodes.size(); i++) {
            childNode = nodes[now].childNodes.get(i);
            if (!isVisited[childNode.at]) {
                if (bfs(nodes, isVisited, paths, childNode.at, end)) {
                    return true;
                }
            }
        }
        return false;
    }

    public static class Node {
        public int at = 0;
        public ArrayList<Node> childNodes;

        public Node(int N) {
            this.at = 0;
            this.childNodes = new ArrayList<>(N - 1);
        }
    }
}