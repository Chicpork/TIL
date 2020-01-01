import java.util.Scanner;

public class boj2455_200101_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int people = 0;
        int max = 0;
        for (int i = 0; i < 4; i++) {
            people -= sc.nextInt();
            people += sc.nextInt();
            if (people > max) {
                max = people;
            }
        }
        System.out.println(max);
    }
}