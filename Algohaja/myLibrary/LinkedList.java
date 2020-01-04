/**
 * 
 * @param <T> type of LinkedList
 */
public class LinkedList<T> {
    private Node first; // 최초 노드 저장
    private Node last; // 마지막 노드 저장
    private int linkedListSize; // 노드 개수 저장

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
            output = this.first.data;
            this.first = this.first.nextNode; // 1개만 있는 경우 null
            this.linkedListSize--;
        } else if (index == this.linkedListSize - 1) {
            output = this.last.data;
            Node nodeAtLastBefore = getNodeAtIndex(index - 1);
            nodeAtLastBefore.nextNode = null;
            this.last = nodeAtLastBefore;
            this.linkedListSize--;
        } else {
            Node nodeAtIndexBefore = getNodeAtIndex(index - 1);
            Node nodeAtIndex = getNodeAtIndex(index);
            output = nodeAtIndex.data;
            nodeAtIndexBefore.nextNode = nodeAtIndex.nextNode;
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
        if (this.first != null) {
            Node tempNode = this.first;
            for (int i = 0; i < this.linkedListSize - 1; i++) {
                output += tempNode.data.toString() + ", ";
                tempNode = tempNode.nextNode;
            }
            output += tempNode.data.toString();
        }
        output += "]";
        return output;
    }
}