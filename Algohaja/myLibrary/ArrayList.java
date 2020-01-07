/**
 * 
 * @param <T> type of arrayList
 */
public class ArrayList<T> {
    private Object[] arrayList;
    private int arrayListSize;

    public ArrayList() {
        this.arrayList = new Object[10];
        this.arrayListSize = 0;
    }

    public ArrayList(int size) {
        if (size < 1) {
            throw new ArrayIndexOutOfBoundsException(size);
        }
        this.arrayList = new Object[size];
        this.arrayListSize = 0;
    }

    public boolean add(T object) {
        if(this.arrayList.length == this.arrayListSize) {
            expandObjectDouble();
        }

        this.arrayList[this.arrayListSize++] = object;
        return true;
    }

    public boolean add(T object, int index) {
        if(index < 0 || index >= this.arrayListSize) {
            return false;
        }

        if(this.arrayList.length == this.arrayListSize) {
            expandObjectDouble();
        }

        for (int i = this.arrayListSize; i > index; i--) {
            this.arrayList[i] = this.arrayList[i-1];
        }

        this.arrayList[index] = object;
        this.arrayListSize++;
        return true;
    }
    
    private void expandObjectDouble() {
        Object[] tempObject = new Object[this.arrayList.length*2];

        for (int i = 0; i < this.arrayList.length; i++) {
            tempObject[i] = this.arrayList[i];
        }

        this.arrayList = tempObject;
    }

    @SuppressWarnings("unchecked")
    public T remove(int index) {
        if(index < 0 || index >= this.arrayListSize) {
            return null;
        }

        T tempObject = (T)this.arrayList[index];
        for (int i = index; i < this.arrayListSize; i++) {
            this.arrayList[i] = this.arrayList[i+1];
        }
        this.arrayListSize--;
        return tempObject;
    }

    @SuppressWarnings("unchecked")
    public T get(int index) {
        if(index < 0 || index >= this.arrayListSize) {
            return null;
        }
        return (T)this.arrayList[index];
    }

    public boolean update(T object, int index) {
        if(index < 0 || index >= this.arrayListSize) {
            return false;
        }
        this.arrayList[index] = object;
        return true;
    }

    public int size() {
        return this.arrayListSize;
    }

    @Override
    public String toString() {
        String output = "[";
        for (int i = 0; i < this.arrayListSize - 1; i++) {
            output += this.arrayList[i].toString() + ", ";
        }
        output += this.arrayList[this.arrayListSize - 1].toString() + "]";
        return output;
    }

    // public static void main(String[] args) {
    //     ArrayList<String> arrayList = new ArrayList<>();
    //     arrayList.add("hi");
    //     arrayList.add("there");
    //     System.out.println(arrayList.size());
    //     System.out.println(arrayList.toString());
    //     System.out.println(arrayList.get(1));
    //     arrayList.update("change",1);
    //     System.out.println(arrayList.toString());
    //     System.out.println(arrayList.remove(0));
    //     System.out.println(arrayList.toString());
    // }
}