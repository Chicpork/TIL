
public class BinaryTree<T> {
    private Node rootNode;

    private class Node {
        private T data;
        private Node leftChild;
        private Node rightChild;

        public Node() {
            this.data = null;
            this.leftChild = null;
            this.rightChild = null;
        }

        public Node(T data) {
            this.data = data;
            this.leftChild = null;
            this.rightChild = null;
        }
    }

    public BinaryTree() {
        rootNode = new Node();
    }

    public BinaryTree(T data) {
        rootNode = new Node(data);
    }

    public void setRoot(T data) {
        rootNode.data = data;
    }

    public void insert(T at, T addData) {
        Node findNode = find(rootNode, at);
        if (findNode != null) {
            if (findNode.leftChild == null) {
                findNode.leftChild = new Node(addData);
            } else if (findNode.rightChild == null) {
                findNode.rightChild = new Node(addData);
            }
        }
    }

    public void insertLeft(T at, T addData) {
        Node findNode = find(rootNode, at);
        if (findNode != null) {
            findNode.leftChild = new Node(addData);
        }
    }

    public void insertRight(T at, T addData) {
        Node findNode = find(rootNode, at);
        if (findNode != null) {
            findNode.rightChild = new Node(addData);
        }
    }

    public void insertBoth(T at, T addDataLeft, T addDataRight) {
        Node findNode = find(rootNode, at);
        if (findNode != null) {
            if (addDataLeft != null) {
                findNode.leftChild = new Node(addDataLeft);
            }
            if (addDataRight != null) {
                findNode.rightChild = new Node(addDataRight);
            }
        }
    }

    public void delete() {

    }

    private Node find(Node node, T data) {
        if (node != null) {
            if (node.data.equals(data)) {
                return node;
            }
            Node returnNode = find(node.leftChild, data);
            if (returnNode != null) {
                return returnNode;
            }
            returnNode = find(node.rightChild, data);
            if (returnNode != null) {
                return returnNode;
            }
        }
        return null;
    }

    public void preOrder() {
        StringBuilder output = new StringBuilder();
        preOrderSelf(rootNode, output);
        System.out.println(output);
    }

    private void preOrderSelf(Node node, StringBuilder output) {
        if (node != null) {
            output.append(node.data.toString());
            preOrderSelf(node.leftChild, output);
            preOrderSelf(node.rightChild, output);
        }
    }

    public void inOrder() {
        StringBuilder output = new StringBuilder();
        inOrderSelf(rootNode, output);
        System.out.println(output);
    }

    private void inOrderSelf(Node node, StringBuilder output) {
        if (node != null) {
            if (node.leftChild != null) {
                inOrderSelf(node.leftChild, output);
            }
            output.append(node.data.toString());
            if (node.rightChild != null) {
                inOrderSelf(node.rightChild, output);
            }
        }
    }

    public void postOrder() {
        StringBuilder output = new StringBuilder();
        postOrderSelf(rootNode, output);
        System.out.println(output);
    }

    private void postOrderSelf(Node node, StringBuilder output) {
        if (node != null) {
            if (node.leftChild != null) {
                postOrderSelf(node.leftChild, output);
            }
            if (node.rightChild != null) {
                postOrderSelf(node.rightChild, output);
            }
            output.append(node.data.toString());
        }
    }
}