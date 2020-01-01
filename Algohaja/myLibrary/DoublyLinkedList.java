/**
 * 
 * @param <T> type of DoublyLinkedList
 */
public class DoublyLinkedList<T> {
    private Node first; // 최초 노드 저장
    private Node last; // 마지막 노드 저장
    private int linkedListSize; // 노드 개수 저장

    public DoublyLinkedList() {
        this.first = null;
        this.last = null;
        this.linkedListSize = 0;
    }

    public DoublyLinkedList(T data) {
        Node node = new Node(data);
        this.first = node;
        this.last = node;
        this.linkedListSize = 1;
    }

    protected Node getFirst() {
        return this.first;
    }

    protected void setFirst(Node node) {
        this.first = node;
    }

    protected Node getLast() {
        return this.last;
    }

    protected void setLast(Node node) {
        this.last = node;
    }

    protected void setLinkedListSize(int linkedListSize) {
        this.linkedListSize = linkedListSize;
    }

    /**
     * insert data at last of arrayList
     * 
     * @param data data you want to insert
     */
    public void add(T data) {
        Node node = new Node(data);

        if (this.linkedListSize == 0) {
            this.first = node;
            this.last = node;
            this.linkedListSize = 1;
        } else {
            node.prevNode = this.last;
            this.last.nextNode = node;
            this.last = node;
            this.linkedListSize++;
        }
    }

    /**
     * insert data at a specific index of arrayList
     * 
     * @param data  data you want to insert
     * @param index the position you want to insert
     */
    public void add(T data, int index) {
        if (index < 0 || index > this.linkedListSize) {
            return;
        }

        Node node = null;
        if (index == 0) {
            node = new Node(data);
            this.first.prevNode = node;
            node.nextNode = this.first;
            this.first = node;
            this.linkedListSize++;
        } else if (index == linkedListSize) {
            this.add(data);
        } else {
            node = new Node(data);
            Node nodeAtIndexBefore = getNodeAtIndex(index - 1);
            node.prevNode = nodeAtIndexBefore;
            node.nextNode = nodeAtIndexBefore.nextNode;
            nodeAtIndexBefore.nextNode.prevNode = node;
            nodeAtIndexBefore.nextNode = node;
            this.linkedListSize++;
        }
    }

    protected Node getNodeAtIndex(int index) {
        Node output = null;

        if (this.linkedListSize / 2 >= index) {
            output = this.first;

            for (int i = 0; i < index; i++) {
                output = output.nextNode;
            }
        } else {
            output = this.last;

            for (int i = this.linkedListSize - 1; i > index; i--) {
                output = output.prevNode;
            }
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
            this.first = this.first.nextNode;
            this.first.prevNode = null;
            this.linkedListSize--;
        } else if (index == linkedListSize - 1) {
            output = this.last.data;
            Node nodeAtLast = getNodeAtIndex(index - 1);
            nodeAtLast.nextNode = null;
            this.last = nodeAtLast;
            this.linkedListSize--;
        } else {
            Node nodeAtIndex = getNodeAtIndex(index);
            output = nodeAtIndex.data;
            nodeAtIndex.nextNode.prevNode = nodeAtIndex.prevNode;
            nodeAtIndex.prevNode.nextNode = nodeAtIndex.nextNode;
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

    protected void setSize(int size) {
        this.linkedListSize = size;
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

    protected class Node {
        private T data; // 데이터 필드
        private Node prevNode; // 이전 노드 저장을 위한 값
        private Node nextNode; // 다음 노드 저장을 위한 값

        public Node(T data) {
            this.data = data;
            this.prevNode = null;
            this.nextNode = null;
        }

        protected T getData() {
            return data;
        }

        protected void setData(T data) {
            this.data = data;
        }

        protected Node getPrevNode() {
            return prevNode;
        }

        protected void setPrevNode(Node prevNode) {
            this.prevNode = prevNode;
        }

        protected Node getNextNode() {
            return nextNode;
        }

        protected void setNextNode(Node nextNode) {
            this.nextNode = nextNode;
        }

        @Override
        public String toString() {
            return this.data.toString();
        }

    }
}