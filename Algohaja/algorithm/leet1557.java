import java.util.ArrayList;
import java.util.List;

public class leet1557 {
    public static void main(String[] args) {
        int n = 5;
        List<List<Integer>> edges = List.of(List.of(0,1),List.of(2,1),List.of(3,1),List.of(1,4),List.of(2,4));

        // List<Node> nodes = new ArrayList<>();
        // for (int i = 0; i < n; i++) {
        //     nodes.add(new Node(i, true));
        // }

        Node[] nodes = new Node[n];

        int start, end;
        for (List<Integer> edge : edges) {
            start = edge.get(0);
            end = edge.get(1);

            if (nodes[start] == null) {
                nodes[start] = new Node(start, true);
            } 

            if (nodes[end] == null) {
                nodes[end] = new Node(end, false);
            } else {
                nodes[end].isRoot = false;
            }
        }

        List<Integer> output = new ArrayList<>();
        for (int i = 0; i < nodes.length; i++) {
            if (nodes[i] != null && nodes[i].isRoot) {
                output.add(i);
            }
        }
    }

    /**
     * Node
     */
    public static class Node {
        public int n;
        public boolean isRoot;

        public Node(int n, boolean isRoot) {
            this.n = n;
            this.isRoot = isRoot;
        }
    }
}
