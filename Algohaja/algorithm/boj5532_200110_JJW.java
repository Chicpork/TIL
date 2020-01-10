import java.util.Scanner;

public class boj5532_200110_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int D = sc.nextInt();

        int days1 = A%C == 0 ? A/C : A/C + 1;
        int days2 = B%D == 0 ? B/D : B/D + 1;
        System.out.println(days1 > days2 ? L - days1 : L - days2);
    }

}