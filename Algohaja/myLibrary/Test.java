/**
 * Test
 */
public class Test {

    public static void main(String[] args) {

        Stack<String> stack = new Stack<>();
        stack.push("1");
        stack.push("2");
        stack.push("3");
        stack.push("4");
        System.out.println(stack.toString());
        
        System.out.println(stack.pop());
        System.out.println(stack.toString());
        
        System.out.println(stack.peek());
        System.out.println(stack.toString());
        
        // CircularLinkedList<String> t = new CircularLinkedList<>();
        // t.add("hi1");
        // t.add("hi2");
        // // t.add("hi3");
        // // t.add("hi4");
        // // t.add("hi5");
        // // t.add("hi6");
        // DoublyLinkedList<String>.DoublyLinkedListIterator tt = t.listIterator();
        // String ts = null;
        // System.out.println(t);
        // while (tt.hasNext()) {
        //     ts = tt.next();
        //     if (ts.equals("hi1")) {
        //         tt.add("hihi");
        //     }
        // }

        // System.out.println(t);

        // CircularLinkedList<String> linkedList = new CircularLinkedList<>();
        // linkedList.add("hi");
        // linkedList.add("here");
        // System.out.println(linkedList.toString());
        // linkedList.add("we");
        // System.out.println(linkedList.toString());
        // linkedList.add("are");
        // System.out.println(linkedList.toString());
        // System.out.println(linkedList.get(2));
        // System.out.println(linkedList.toString());
        // System.out.println(linkedList.get(4));
        // System.out.println(linkedList.toString());
        // linkedList.update("change", 1);
        // System.out.println(linkedList.toString());
        // linkedList.add("123123", 2);
        // System.out.println(linkedList.toString());
        // System.out.println(linkedList.remove(1));
        // System.out.println(linkedList.toString());
        // System.out.println(linkedList.remove(3));
        // System.out.println(linkedList.toString());
        // System.out.println(linkedList.remove(2));
        // System.out.println(linkedList.toString());
        // System.out.println(linkedList.remove(0));
        // System.out.println(linkedList.toString());
        // System.out.println(linkedList.remove(0));
        // System.out.println(linkedList.toString());
    }
}