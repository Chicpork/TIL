/**
 * 
 * @param <T> type of DoublyLinkedList
 */
public class DoublyLinkedList<T> {
    private Node firstNode; // 최초 노드 저장
    private Node lastNode; // 마지막 노드 저장
    private int linkedListSize; // 노드 개수 저장

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

    public class DoublyLinkedListIterator {
        protected Node lastNode;
        protected Node lastNextNode;
        protected int lastNextIndex;

        public DoublyLinkedListIterator() {
            lastNode = null;
            lastNextNode = firstNode;
            lastNextIndex = 0;
        }

        public DoublyLinkedListIterator(int index) {
            lastNextNode = getNodeAtIndex(index);
            lastNode = lastNextNode.prevNode;
            lastNextIndex = index + 1;
        }

        public boolean hasNext() {
            return lastNextIndex < linkedListSize;
        }

        public T next() {
            if (!hasNext()) {
                return null;
            }
            lastNode = lastNextNode;
            lastNextNode = lastNextNode.nextNode;
            lastNextIndex++;
            return lastNode.data;
        }

        public void add(T data) {
            DoublyLinkedList.this.add(data, lastNextIndex);
            lastNextNode = lastNode.nextNode;
        }

        public T remove() {
            return DoublyLinkedList.this.remove(--lastNextIndex);
        }
    }

    public DoublyLinkedList() {
        this.firstNode = null;
        this.lastNode = null;
        this.linkedListSize = 0;
    }

    public DoublyLinkedList(T data) {
        Node node = new Node(data);
        this.firstNode = node;
        this.lastNode = node;
        this.linkedListSize = 1;
    }

    protected Node getFirst() {
        return this.firstNode;
    }

    protected void setFirst(Node node) {
        this.firstNode = node;
    }

    protected Node getLast() {
        return this.lastNode;
    }

    protected void setLast(Node node) {
        this.lastNode = node;
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
            this.firstNode = node;
            this.lastNode = node;
            this.linkedListSize = 1;
        } else {
            node.prevNode = this.lastNode;
            this.lastNode.nextNode = node;
            this.lastNode = node;
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
            throw new ArrayIndexOutOfBoundsException(index);
        }

        Node node = null;
        if (index == 0) {
            node = new Node(data);
            this.firstNode.prevNode = node;
            node.nextNode = this.firstNode;
            this.firstNode = node;
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
            output = this.firstNode;

            for (int i = 0; i < index; i++) {
                output = output.nextNode;
            }
        } else {
            output = this.lastNode;

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
            throw new ArrayIndexOutOfBoundsException(index);
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
            throw new ArrayIndexOutOfBoundsException(index);
        }

        T output = null;
        if (this.linkedListSize == 1) {
            output = this.firstNode.data;
            this.firstNode = null;
            this.lastNode = null;
            this.linkedListSize = 0;
        } else {
            if (index == 0) {
                output = this.firstNode.data;
                this.firstNode = this.firstNode.nextNode;
                this.firstNode.prevNode = null;
                this.linkedListSize--;
            } else if (index == linkedListSize - 1) {
                output = this.lastNode.data;
                Node nodeAtLast = getNodeAtIndex(index - 1);
                nodeAtLast.nextNode = null;
                this.lastNode = nodeAtLast;
                this.linkedListSize--;
            } else {
                Node nodeAtIndex = getNodeAtIndex(index);
                output = nodeAtIndex.data;
                nodeAtIndex.nextNode.prevNode = nodeAtIndex.prevNode;
                nodeAtIndex.prevNode.nextNode = nodeAtIndex.nextNode;
                this.linkedListSize--;
            }
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
        if (this.firstNode != null) {
            Node tempNode = this.firstNode;
            for (int i = 0; i < this.linkedListSize - 1; i++) {
                output += tempNode.data.toString() + ", ";
                tempNode = tempNode.nextNode;
            }
            output += tempNode.data.toString();
        }
        output += "]";
        return output;
    }

    public DoublyLinkedListIterator listIterator() {
        return new DoublyLinkedListIterator();
    }
}