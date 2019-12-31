/**
 * ArrayList
 */
public class ArrayList {
    private Object[] arrayList;
    private int arrayListSize;

    public ArrayList() {
        this.arrayList = new Object[10];
        this.arrayListSize = 0;
    }

    public ArrayList(int size) {
        this.arrayList = new Object[size];
        this.arrayListSize = 0;
    }

    public boolean add(Object object, int index) {
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
    
    private boolean expandObjectDouble() {
        tempObject = new Object[this.arrayList.length*2];

        for (int i = 0; i < this.arrayList.length; i++) {
            tempObject[i] = object[i];
        }

        this.arrayList = tempObject;
    }

    public Object remove(int index) {
        if(index < 0 || index >= this.arrayListSize) {
            return null;
        }

        tempObject = arrayList[index];
        for (int i = this.arrayListSize; i > index; i--) {
            this.arrayList[i-1] = this.arrayList[i];
        }

        this.arrayListSize--;
        return tempObject;
    }

    public Object get(int index) {
        return this.arrayList[index];
    }

    public int size() {
        return this.arrayListSize;
    }
}