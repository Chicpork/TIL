import java.util.Scanner;

public class boj1526_200110_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String number = sc.nextLine();
        if (number.matches("[47]*")) {
            System.out.println(number);
            return;
        }

        int N = Integer.parseInt(number);
        int n4 = 0;
        int n7 = 0;
        int output = 0;
        for (int i = 0; i < number.length(); i++) {
            n4 += 4*Math.pow(10,i);
            n7 += 7*Math.pow(10,i);
        }

        if (N > n7) {
            output = n7;
        } else if (N < n4) {
            output = n7/10;
        } else {
            int cnt = number.length() - 1;
            int temp1 = 0;
            int temp2 = 0;
            while (cnt >= 0) {
                temp1 = change(n7, 4, cnt);
                temp2 = change(n4, 7, cnt);

                if (N > temp1) {
                    n4 = temp1;
                } else if (N < temp1 && N > temp2) {
                    n4 = temp2;
                    break;
                } else {
                    n7 = temp2;
                }
                cnt -= 1;
                // System.out.print(n7);
                // System.out.print("  ");
                // System.out.println(n4);
            }
            output = n4;
        }
        
        System.out.println(output);
    }

    public static int change(int src, int number, int size) {
        int temp = (int)Math.pow(10, size);
        int output = (src/temp)*temp;
        for (int i = 0; i < size; i++) {
            output += number*Math.pow(10,i);
        }
        return output;
    }
}