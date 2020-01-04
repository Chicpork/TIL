/**
 * 
 * @param <T> type of CircularLinkedList
 */
public class CircularLinkedList<T> extends DoublyLinkedList<T> {

    public CircularLinkedList() {
        super();
    }

    public CircularLinkedList(T data) {
        super(data);
    }

    @Override
    public T get(int index) {
        index = getCircularIndex(index);
        return super.get(index);
    }

    /**
     * insert data at last of arrayList
     * 
     * @param data data you want to insert
     */
    @Override
    public void add(T data) {
        super.add(data);
        super.getFirst().setPrevNode(super.getLast());
        super.getLast().setNextNode(super.getFirst());
    }

    /**
     * insert data at a specific index of arrayList
     * 
     * @param data  data you want to insert
     * @param index the position you want to insert
     */
    @Override
    public void add(T data, int index) {
        index = getCircularIndex(index);

        if (index == 0) {
            super.add(data, index);
            super.getFirst().setPrevNode(super.getLast());
            super.getLast().setNextNode(super.getFirst());
        } else if (index == super.getSize()) {
            this.add(data);
        } else {
            super.add(data, index);
        }
    }

    @Override
    public T remove(int index) {
        index = getCircularIndex(index);

        T tempT = super.remove(index);

        if (super.getSize() > 0) {
            if (index == 0) {
                super.getFirst().setPrevNode(super.getLast());
            } else if (index == super.getSize() - 1) {
                super.getLast().setNextNode(super.getFirst());
            }
        }

        return tempT;
    }

    private int getCircularIndex(int index) {
        if (index > super.getSize() - 1) {
            index %= super.getSize();
        }
        return index;
    }
}