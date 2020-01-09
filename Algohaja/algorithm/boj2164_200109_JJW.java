import java.util.LinkedList;
import java.util.Scanner;

public class boj2164_200109_JJW {

    public static void main(String[] args) {
        solve2();
    }

    public static void solve1() {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int pow2 = 1;
        while (pow2 < N) {
            pow2 *= 2;
        }
        System.out.println(pow2 == N ? pow2 : (N - pow2/2)*2);
    }

    public static void solve2() {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        LinkedList<Integer> queue = new LinkedList<Integer>();

        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }
        
        while (queue.size() > 1) {
            queue.poll();
            queue.offer(queue.poll());
        }
        System.out.println(queue.peek());
    }
}