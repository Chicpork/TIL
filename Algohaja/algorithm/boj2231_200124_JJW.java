import java.util.Scanner;

public class boj2231_200124_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int inputNum = Integer.parseInt(sc.nextLine());
        int answer = 0;
        for (int i = 1; i <= inputNum; i++) {
            if (sum(i) + i == inputNum) {
                answer = i;
                break;
            }
        }
        System.out.println(answer);
    }

    public static int sum(int inputNum) {
        int outputNum = 0;
        while (inputNum > 0) {
            outputNum += inputNum % 10;
            inputNum = inputNum / 10;
        }
        return outputNum;
    }
}