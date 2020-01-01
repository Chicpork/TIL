/**
 * 
 * @param <T> type of LinkedList
 */
public class LinkedList<T> {
    private Node first; // 최초 노드 저장
    private Node last; // 마지막 노드 저장
    private int linkedListSize; // 노드 개수 저장

    public LinkedList() {
        this.first = null;
        this.last = null;
        this.linkedListSize = 0;
    }

    public LinkedList(T data) {
        Node node = new Node(data);
        this.first = node;
        this.last = node;
        this.linkedListSize = 1;
    }

    /**
     * insert data at last of arrayList
     * 
     * @param data data you want to insert
     */
    public void add(T data) {
        Node node = new Node(data);
        this.last.nextNode = node;
        this.last = node;
        this.linkedListSize++;
    }

    /**
     * insert data at a specific index of arrayList
     * 
     * @param data  data you want to insert
     * @param index the position you want to insert
     */
    public void add(T data, int index) {
        if (index < 0 || index >= this.linkedListSize) {
            return;
        }

        Node node = null;
        if (index == 0) {
            node = new Node(data);
            node.nextNode = this.first;
            this.first = node;
            this.linkedListSize++;
        } else if (index == linkedListSize) {
            this.add(data);
        } else {
            node = new Node(data);
            Node nodeAtIndexBefore = getNodeAtIndex(index - 1);
            node.nextNode = nodeAtIndexBefore.nextNode;
            nodeAtIndexBefore.nextNode = node;
            this.linkedListSize++;
        }
    }

    private Node getNodeAtIndex(int index) {
        Node output = this.first;
        for (int i = 0; i < index; i++) {
            output = output.nextNode;
        }
        return output;
    }

    /**
     * get data at index
     * 
     * @param index
     * @return the data you find
     */
    public T get(int index) {
        if (index < 0 || index >= this.linkedListSize) {
            return null;
        }

        return getNodeAtIndex(index).data;
    }

    /**
     * update data at index
     * 
     * @param data
     * @param index
     * @return if data was removed, return true, else false
     */
    public boolean update(T data, int index) {
        if (index < 0 || index >= this.linkedListSize) {
            return false;
        }

        getNodeAtIndex(index).data = data;
        return true;
    }

    /**
     * remove data at index
     * 
     * @param index
     * @return the removed data
     */
    public T remove(int index) {
        if (index < 0 || index >= this.linkedListSize) {
            return null;
        }

        T output = null;
        if (index == 0) {
            this.first = this.first.nextNode;
            output = this.first.data;
            this.linkedListSize--;
        } else if (index == linkedListSize-1) {
            Node nodeAtLast = getNodeAtIndex(index - 1);
            nodeAtLast.nextNode = null;
            this.last = nodeAtLast;
            output = this.last.data;
            this.linkedListSize--;
        } else {
            Node nodeAtIndexBefore = getNodeAtIndex(index - 1);
            Node nodeAtIndex = getNodeAtIndex(index);
            nodeAtIndexBefore.nextNode = nodeAtIndex.nextNode;
            output = nodeAtIndex.data;
            this.linkedListSize--;
        }
        return output;
    }

    /**
     * return size of arrayList
     * 
     * @return size of arrayList
     */
    public int getSize() {
        return this.linkedListSize;
    }

    @Override
    public String toString() {
        String output = "[";
        Node tempNode = this.first;
        for (int i = 0; i < this.linkedListSize - 1; i++) {
            output += tempNode.data.toString() + ", ";
            tempNode = tempNode.nextNode;
        }
        output += tempNode.data.toString();
        output += "]";
        return output;
    }

    private class Node {
        private T data; // 데이터 필드
        private Node nextNode; // 다음 노드 저장을 위한 값

        public Node(T data) {
            this.data = data;
            this.nextNode = null;
        }

        @Override
        public String toString() {
            return this.data.toString();
        }
    }

    private class LinkedListIterator {
        private Node next;
        private int nextIndex;

        public LinkedListIterator() {
            next = first;
            nextIndex = 1;

        }

        public boolean hasNext() {
            if (nextIndex >= linkedListSize) {
                return false;
            }
            return true;
        }

        public T next() {
            T data = next.data;
            next = next.nextNode;
            nextIndex++;
            return data;
        }

        public void add(T data) {
            Node node = new Node(data);
            if (next.nextNode == null) {
                next.nextNode = node;
            } else {
                node.nextNode = next.nextNode;
                next.nextNode = node;
            }

            linkedListSize++;
            this.nextIndex++;
        }

        public T remove() {
            return LinkedList.this.remove(nextIndex - 1);
        }
    }
}