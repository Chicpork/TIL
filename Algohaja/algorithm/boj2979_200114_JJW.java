import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class boj2979_200114_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        List<Integer> costs = new ArrayList<>(4);
        costs.add(0);
        Arrays.stream(sc.nextLine().split(" ")).forEach(s -> costs.add(Integer.parseInt(s)));
        
        String[] inOutTemp = null;
        int maxTime = 0;
        int[] inTime = new int[3];
        int[] outTime = new int[3];
        for (int i = 0; i < 3; i++) {
            inOutTemp = sc.nextLine().split(" ");
            inTime[i] = Integer.parseInt(inOutTemp[0]);
            outTime[i] = Integer.parseInt(inOutTemp[1]);
            if (maxTime < outTime[i]) {
                maxTime = outTime[i];
            }
        }
        int[] times = new int[maxTime];

        for (int i = 0; i < 3; i++) {
            for (int j = inTime[i]; j < outTime[i]; j++) {
                times[j] += 1;
            }
        }

        int output = 0;
        for (int i = 0; i < times.length; i++) {
            output += costs.get(times[i])*times[i];
        }
        System.out.println(output);
    }
}