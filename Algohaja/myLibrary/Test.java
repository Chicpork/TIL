/**
 * Test
 */
public class Test {

    public static void main(String[] args) {
        CircularLinkedList<String> linkedList = new CircularLinkedList<>("hi");
        linkedList.add("here");
        linkedList.add("we");
        linkedList.add("are");
        System.out.println(linkedList.toString());
        System.out.println(linkedList.get(2));
        System.out.println(linkedList.toString());
        linkedList.update("change", 1);
        System.out.println(linkedList.toString());
        linkedList.add("123123", 2);
        System.out.println(linkedList.toString());
        System.out.println(linkedList.remove(1));
        System.out.println(linkedList.toString());
        System.out.println(linkedList.remove(3));
        System.out.println(linkedList.toString());
        System.out.println(linkedList.remove(2));
        System.out.println(linkedList.toString());
        System.out.println(linkedList.remove(0));
        System.out.println(linkedList.toString());
    }
}