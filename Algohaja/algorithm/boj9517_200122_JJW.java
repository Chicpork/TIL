import java.util.Scanner;

public class boj9517_200122_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = Integer.parseInt(sc.nextLine());
        int N = Integer.parseInt(sc.nextLine());

        int maxPeople = 8;
        int maxTime = 210;

        String[] answers = null;
        int passedTime = 0;
        for (int i = 0; i < N; i++) {
            answers = sc.nextLine().split(" ");
            passedTime += Integer.parseInt(answers[0]);
            if (passedTime >= maxTime) {
                break;
            }
            if (answers[1].equals("T")) {
                K = K + 1 > maxPeople ? 1 : K + 1;
            }
        }
        System.out.println(K);
    }
}