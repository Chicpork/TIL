public class Stack<T> {
    private Object[] stack;
    private int stackIndex;
    private int stackMaxSize;

    public Stack() {
        stackMaxSize = 10;
        stackIndex = -1;
        stack = new Object[stackMaxSize];
    }

    public Stack(int size) {
        if (size < 1) {
            throw new ArrayIndexOutOfBoundsException(size);
        }
        stackMaxSize = size;
        stackIndex = -1;
        stack = new Object[stackMaxSize];
    }

    public boolean isEmpty() {
        if (stackIndex == -1) {
            return true;
        }
        return false;
    }

    @SuppressWarnings("unchecked")
    public T pop() {
        if (isEmpty()) {
            return null;
        }
        T tempT = (T) stack[stackIndex];
        stack[stackIndex--] = null;
        return tempT;
    }

    public boolean isFull() {
        if (stackIndex == stackMaxSize - 1) {
            return true;
        }
        return false;
    }

    public void push(T data) {
        if (isFull()) {
            return;
        }
        stack[++stackIndex] = data;
    }

    @SuppressWarnings("unchecked")
    public T peek() {
        return (T) stack[stackIndex];
    }

    @Override
    public String toString() {
        if (isEmpty()) {
            return "<>";
        }

        String output = "<";
        for (int i = 0; i < stackIndex; i++) {
            output += stack[i].toString() + ", ";
        }
        output += stack[stackIndex].toString() + ">";
        return output;
    }
}