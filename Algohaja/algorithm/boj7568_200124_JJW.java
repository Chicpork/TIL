import java.util.Scanner;

public class boj7568_200124_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int people = Integer.parseInt(sc.nextLine());

        int[][] lists = new int[people][2];
        String[] person = null;
        for (int k = 0; k < people; k++) {
            person = sc.nextLine().split(" ");
            lists[k][0] = Integer.parseInt(person[0]);
            lists[k][1] = Integer.parseInt(person[1]);
        }

        int number = 0;
        for (int k = 0; k < people; k++) {
            number = 1;
            for (int k2 = 0; k2 < people; k2++) {
                if (k != k2) {
                    if ( lists[k][0] < lists[k2][0] && lists[k][1] < lists[k2][1]) {
                        number += 1;
                    }
                }
            }
            System.out.print(number + " ");
        }
    }
}
