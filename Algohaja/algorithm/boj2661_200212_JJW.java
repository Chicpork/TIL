import java.util.Scanner;

public class boj2661_200212_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] seq = new int[N];
        backtracking(seq, 0, N);
        for (int i = 0; i < seq.length; i++) {
            System.out.print(seq[i]);
        }
    }

    public static boolean backtracking(int[] seq, int depth, int N) {
        if(depth == N) {
            return true;
        }

        for (int i = 1; i <= 3; i++) {
            if(depth > 0 && seq[depth-1] == i) {
                continue;
            }
            seq[depth] = i;
            if(isGoodSeq(seq, depth+1)) {
                if(backtracking(seq, depth+ 1, N)) {
                    return true;
                }
                seq[depth] = 0;
            }
        }

        return false;
    }

    public static boolean isGoodSeq(int[] seq, int depth) {
        boolean same;
        for (int i = 2; i <= depth/2; i++) {
            for (int j = 0; j <= depth - 2*i; j++) {
                same = true;
                for (int j2 = 0; j2 < i; j2++) {
                    if(seq[j+j2] != seq[j+j2+i]) {
                        same = false;
                        break;
                    }
                }
                if (same) {
                    return false;
                }
            }
        }
        return true;
    }
}