import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.NoSuchElementException;

public class boj1260_200210_JJW {

    public static class Tree {
        private Node rootNode;
        private HashMap<Integer, Node> nodes;

        private class Node {
            private Integer data;
            private LinkedList<Node> children;

            public Node() {
                this.data = null;
                this.children = new LinkedList<>();
            }

            public Node(Integer data) {
                this.data = data;
                this.children = new LinkedList<>();
            }

            public void add(Node addNode) {
                if (this.children.size() == 0) {
                    this.children.add(addNode);
                } else {
                    ListIterator<Node> iter = this.children.listIterator();
                    boolean isAdded = false;
                    while (iter.hasNext()) {
                        if (iter.next().data.intValue() > addNode.data.intValue()) {
                            this.children.add(iter.previousIndex(), addNode);
                            isAdded = true;
                            break;
                        }
                    }
                    if (!isAdded) {
                        this.children.add(addNode);
                    }
                }
            }

        }

        public Tree() {
            rootNode = new Node();
            nodes = new HashMap<>();
        }

        public Tree(Integer data) {
            rootNode = new Node(data);
            nodes = new HashMap<>();
            nodes.put(data, rootNode);
        }

        public void setRoot(Integer data) {
            rootNode.data = data;
            nodes = new HashMap<>();
            nodes.put(data, rootNode);
        }

        public void insert(Integer x1, Integer x2) {
            Node findNode = find(rootNode, x1);
            if (findNode != null) {
                if (findNode.children.size() == 0) {
                    findNode.children.add(new Node(x2));
                } else {
                    ListIterator<Node> iter = findNode.children.listIterator();
                    boolean isAdded = false;
                    while (iter.hasNext()) {
                        if (iter.next().data.intValue() > x2.intValue()) {
                            iter.add(new Node(x2));
                            isAdded = true;
                            break;
                        }
                    }
                    if (!isAdded) {
                        findNode.children.add(new Node(x2));
                    }
                }
            } else {
                throw new IndexOutOfBoundsException();
            }
        }

        // find using dfs
        private Node find(Node node, Integer data) {
            if (node != null) {
                if (node.data.equals(data)) {
                    return node;
                }
                Node returnNode = null;
                if (node.children.size() > 0) {
                    for (Node child : node.children) {
                        returnNode = find(child, data);
                        if (returnNode != null) {
                            return returnNode;
                        }
                    }
                }
            }
            return null;
        }

        // insertChildNode using hashmap
        private void insertChildNode(Integer at, Integer addData) {
            Node findNode = nodes.get(at);
            if (findNode == null) {
                findNode = new Node(at);
                nodes.put(at, findNode);
            }

            Node addNode = nodes.get(addData);
            if (addNode == null) {
                addNode = new Node(addData);
                nodes.put(addData, addNode);
            }

            findNode.add(addNode);
            addNode.add(findNode);
        }

        public void printDfs() {
            StringBuilder output = new StringBuilder();
            HashSet<Integer> isVisited = new HashSet<>(nodes.size());
            dfs(rootNode, output, isVisited);
            System.out.println(output);
        }

        private void dfs(Node node, StringBuilder output, HashSet<Integer> isVisited) {
            if (node != null) {
                isVisited.add(node.data);
                output.append(node.data + " ");
                if (node.children.size() > 0) {
                    for (Node child : node.children) {
                        if (!isVisited.contains(child.data)) {
                            dfs(child, output, isVisited);
                        }
                    }
                }
            }
        }

        public void printBfs() {
            StringBuilder output = new StringBuilder();
            HashSet<Integer> isVisited = new HashSet<>(nodes.size());
            Queue<Node> queue = new Queue<>();
            queue.push(rootNode);
            Node tempNode = null;
            while (!queue.isEmpty()) {
                tempNode = queue.pop();
                output.append(tempNode.data + " ");
                isVisited.add(tempNode.data);
                if (tempNode.children.size() > 0) {
                    for (Node child : tempNode.children) {
                        if (!isVisited.contains(child.data)) {
                            queue.push(child);
                            isVisited.add(child.data);
                        }
                    }
                }
            }
            System.out.println(output);
        }
    }

    public static class Queue<T> {
        private Node firstNode; // 최초 노드 저장
        private Node lastNode; // 마지막 노드 저장
        private int size; // 노드 개수 저장

        protected class Node {
            private T data; // 데이터 필드
            private Node prevNode; // 이전 노드 저장을 위한 값
            private Node nextNode; // 다음 노드 저장을 위한 값

            public Node(T data) {
                this.data = data;
                this.prevNode = null;
                this.nextNode = null;
            }

            @Override
            public String toString() {
                return this.data.toString();
            }
        }

        public void Queue() {
            firstNode = null;
            lastNode = null;
            size = 0;
        }

        public void Queue(T data) {
            firstNode = new Node(data);
            lastNode = firstNode;
            size = 1;
        }

        public boolean isEmpty() {
            return firstNode == null ? true : false;
        }

        public void push(T data) {
            if (firstNode == null) {
                firstNode = new Node(data);
                lastNode = firstNode;
                size = 1;
            } else {
                lastNode.nextNode = new Node(data);
                lastNode.nextNode.prevNode = lastNode;
                lastNode = lastNode.nextNode;
                size += 1;
            }
        }

        public T pop() {
            if (isEmpty()) {
                throw new NoSuchElementException();
            }

            T tempT = firstNode.data;
            firstNode = firstNode.nextNode;
            size -= 1;
            return tempT;
        }

        public T peek() {
            if (isEmpty()) {
                return null;
            }
            return firstNode.data;
        }

        public int size() {
            return size;
        }

        public T back() {
            if (isEmpty()) {
                return null;
            }
            return lastNode.data;
        }

        @Override
        public String toString() {
            String output = "[";
            if (!isEmpty()) {
                Node tempNode = firstNode;
                while (tempNode != lastNode) {
                    output += tempNode.data.toString() + ", ";
                    tempNode = tempNode.nextNode;
                }
                output += lastNode.data.toString();
            }
            output += "]";
            return output;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] NMV = bf.readLine().split(" ");
        int N = Integer.parseInt(NMV[0]);
        int M = Integer.parseInt(NMV[1]);
        int V = Integer.parseInt(NMV[2]);
        String[] nums = null;
        Tree tree = new Tree(V);
        for (int i = 0; i < M; i++) {
            nums = bf.readLine().split(" ");
            tree.insertChildNode(Integer.parseInt(nums[0]), Integer.parseInt(nums[1]));
        }
        tree.printDfs();
        tree.printBfs();
    }
}