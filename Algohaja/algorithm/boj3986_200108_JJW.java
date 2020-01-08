import java.util.Scanner;
import java.util.Stack;

public class boj3986_200108_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        String input = null;
        Stack<Character> stack = null;
        int output = 0;
        for (int i = 0; i < N; i++) {
            input = sc.nextLine();
            stack = new Stack<>();
            stack.push('T');
            for (int j = 0; j < input.length(); j++) {
                if (input.charAt(j) == 'A') {
                    if (stack.peek() == 'A') {
                        stack.pop();
                    } else {
                        stack.push('A');
                    }
                } else {
                    if (stack.peek() == 'B') {
                        stack.pop();
                    } else {
                        stack.push('B');
                    }
                }
            }
            if (stack.size() == 1) {
                output += 1;
            }
        }
        System.out.println(output);
    }

}