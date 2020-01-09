import java.util.Scanner;

public class boj1094_200109_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int len = 64;
        int tempLen = 0;
        int cnt = 0;
        while (tempLen != X) {
            if (len <= X && tempLen + len <= X) {
                tempLen += len;
                cnt += 1;
            }
            len /= 2;
        }
        System.out.println(cnt);
    }
    
}