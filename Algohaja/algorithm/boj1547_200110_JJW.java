import java.util.Scanner;

public class boj1547_200110_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = Integer.parseInt(sc.nextLine());
        String ballCup = "1";
        String tempS[] = null;
        for (int i = 0; i < M; i++) {
            tempS = sc.nextLine().split(" ");
            if( tempS[0].equals(ballCup)) {
                ballCup = tempS[1];
                continue;
            }
            if( tempS[1].equals(ballCup)) {
                ballCup = tempS[0];
                continue;
            }
        }
        System.out.println(ballCup);
    }
}