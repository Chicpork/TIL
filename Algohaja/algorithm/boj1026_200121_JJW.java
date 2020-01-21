import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class boj1026_200121_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());

        String[] temp1 = sc.nextLine().split(" ");
        String[] temp2 = sc.nextLine().split(" ");
        Integer[] num1 = new Integer[N];
        Integer[] num2 = new Integer[N];
        
        for (int i = 0; i < N; i++) {
            num1[i] = Integer.parseInt(temp1[i]);
        }
        for (int i = 0; i < N; i++) {
            num2[i] = Integer.parseInt(temp2[i]);
        }

        Arrays.sort(num1);
        Arrays.sort(num2, Collections.reverseOrder());

        int output = 0;
        for (int i = 0; i < N; i++) {
            output += num1[i]*num2[i];
        }
        System.out.println(output);
    }
}