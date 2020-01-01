import java.util.LinkedList;
import java.util.Scanner;

public class boj1158_200101_JJW {

    public static void main(String[] args) {
        LinkedList<Integer> clList = new LinkedList<>();

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        for (int i = 1; i <= N; i++) {
            clList.add(i);
        }

        String output = "<";
        int index = K - 1;
        output += String.valueOf(clList.remove(index));
        while (clList.size() >= 1) {
            index += K - 1;
            if (index > clList.size()-1) {
                index %= clList.size();
            }
            output += ", " + String.valueOf(clList.remove(index));
        }
        output += ">";
        System.out.println(output);
    }
}