import java.util.Scanner;

public class boj1592_200110_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int L = sc.nextInt();

        int[] getBalls = new int[N];
        getBalls[0] = 1;
        int lastBall = 0;
        int cnt = 0;
        while (true) {
            lastBall = getBalls[lastBall] % 2 == 1 ? lastBall + L : lastBall - L;

            if (lastBall < 0) {
                lastBall = N + lastBall;
            } else if (lastBall >= N) {
                lastBall = lastBall - N;
            }
            getBalls[lastBall] += 1;
            cnt += 1;
            if (getBalls[lastBall] == M) {
                break;
            }
        }
        System.out.println(cnt);
    }

}