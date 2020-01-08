import java.util.Scanner;

public class boj10799_200108_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String in = sc.next();
        int output = 0;
        int size = -1;
        for (int i = 0; i < in.length()-1; i++) {
            if (in.charAt(i) == '(') {
                size++;
            } else {
                size--;
            }
            if (in.substring(i, i+2).equals("()")) {
                output += size;
            } else if (in.substring(i, i+2).equals("))")) {
                output++;
            }
        }
        System.out.println(output);
    }
}