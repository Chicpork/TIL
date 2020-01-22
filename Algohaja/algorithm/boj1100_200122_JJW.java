import java.util.Scanner;

public class boj1100_200122_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = null;
        int cnt = 0;
        for (int i = 0; i < 8; i++) {
            s = sc.nextLine();
            for (int j = 0 + i%2; j < s.length(); j += 2) {
                if (s.charAt(j) == 'F') {
                    cnt += 1;
                }
            }
        }
        System.out.println(cnt);
    }
}