import java.util.LinkedList;
import java.util.Scanner;

public class boj2161_200110_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        LinkedList<Integer> queue = new LinkedList<Integer>();

        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }
        while (queue.size() > 1) {
            System.out.print(queue.poll() + " ");
            queue.offer(queue.poll());
        }
        System.out.print(queue.peek());
    }

}