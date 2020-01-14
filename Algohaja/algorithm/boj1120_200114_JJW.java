import java.util.Scanner;

public class boj1120_200114_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] in = sc.nextLine().split(" ");
        String A = in[0];
        String B = in[1];

        int cnt = 0;
        int maxCnt = 0;
        for (int i = 0; i <= B.length() - A.length(); i++) {
            cnt = 0;
            for (int j = 0; j < A.length(); j++) {
                if (A.charAt(j) == B.charAt(i + j)) {
                    cnt += 1;
                }
            }
            if (maxCnt < cnt) {
                maxCnt = cnt;
            }
        }
        System.out.println(A.length() - maxCnt);

        sc.close();
    }
}