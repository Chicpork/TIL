import java.util.Scanner;

public class boj1436_200124_JJW {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int series = Integer.parseInt(sc.nextLine());

        int num = 0;
        while(series > 0) {
            num += 1;
            if (String.valueOf(num).contains("666")) {
                series -= 1;
            }
        }
        System.out.println(num);
    }
}
