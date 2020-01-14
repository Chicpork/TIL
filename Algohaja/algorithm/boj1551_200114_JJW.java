import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Scanner;

public class boj1551_200114_JJW {

    public static void main(String[] args) {
        solve2();
    }

    public static void solve1() {
        Scanner sc = new Scanner(System.in);
        String[] in = sc.nextLine().split(" ");
        String[] in2 = sc.nextLine().split(",");
        int N = Integer.parseInt(in[0]);
        int K = Integer.parseInt(in[1]);
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < in2.length; i++) {
            list.add(Integer.parseInt(in2[i]));
        }

        LinkedList<Integer> tempList = null;
        int left, right = 0;
        for (int i = 0; i < K; i++) {
            tempList = new LinkedList<>();
            left = 0;
            right = 0;
            ListIterator<Integer> listIterator = list.listIterator();
            if (listIterator.hasNext()) {
                left = listIterator.next();
            }
            while (listIterator.hasNext()) {
                right = listIterator.next();
                tempList.add(right - left);
                left = right;
            }
            list = tempList;
        }

        ListIterator<Integer> listIterator = list.listIterator();
        if (listIterator.hasNext()) {
            System.out.print(listIterator.next());
        }
        while (listIterator.hasNext()) {
            System.out.print(",");
            System.out.print(listIterator.next());
        }
    }

    public static void solve2() {
        Scanner sc = new Scanner(System.in);
        String[] in = sc.nextLine().split(" ");
        String[] in2 = sc.nextLine().split(",");
        int N = Integer.parseInt(in[0]);
        int K = Integer.parseInt(in[1]);
        int[] arr = new int[N];
        for (int i = 0; i < in2.length; i++) {
            arr[i] = Integer.parseInt(in2[i]);
        }

        for (int i = 0; i < K; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                arr[j] = arr[j+1] - arr[j];
            }
        }

        System.out.print(arr[0]);
        for (int i = 1; i < N - K; i++) {
            System.out.print("," + arr[i]);
        }
    }
}