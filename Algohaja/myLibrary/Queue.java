import java.util.NoSuchElementException;

public class Queue<T> {
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
            lastNode.nextNode.prevNode  = lastNode;
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