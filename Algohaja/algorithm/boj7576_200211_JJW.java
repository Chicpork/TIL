import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class boj7576_200211_JJW {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] MN = bf.readLine().split(" ");
        String[] temp = null;
        int M = Integer.parseInt(MN[0]);
        int N = Integer.parseInt(MN[1]);
        int[][] box = new int[N][M];
        LinkedList<int[]> grownUp = new LinkedList<>(); // (N, M, depth)
        for (int i = 0; i < N; i++) {
            temp = bf.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                box[i][j] = Integer.parseInt(temp[j]);
                if (box[i][j] == 1) {
                    grownUp.add(new int[] { i, j, 0 });
                }
            }
        }
        int depth = bfs(box, grownUp, N, M);

        // printBox(box);
        System.out.println(checkBox(box) ? depth : -1);
    }

    public static void printBox(int[][] box) {
        for (int i = 0; i < box.length; i++) {
            for (int j = 0; j < box[i].length; j++) {
                System.out.print(box[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static boolean checkBox(int[][] box) {
        for (int i = 0; i < box.length; i++) {
            for (int j = 0; j < box[i].length; j++) {
                if (box[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public static int bfs(int[][] box, LinkedList<int[]> grownUp, int N, int M) {
        int[] temp = null;
        int depth = 0;
        while (!grownUp.isEmpty()) {
            temp = grownUp.pop();

            if (temp[0] - 1 >= 0 && box[temp[0] - 1][temp[1]] == 0) { // 왼쪽
                grownUp.add(new int[] { temp[0] - 1, temp[1], temp[2] + 1 });
                box[temp[0] - 1][temp[1]] = 1;
                depth = temp[2] + 1;
            }
            if (temp[0] + 1 < N && box[temp[0] + 1][temp[1]] == 0) { // 오른쪽
                grownUp.add(new int[] { temp[0] + 1, temp[1], temp[2] + 1 });
                box[temp[0] + 1][temp[1]] = 1;
                depth = temp[2] + 1;
            }
            if (temp[1] - 1 >= 0 && box[temp[0]][temp[1] - 1] == 0) { // 아래
                grownUp.add(new int[] { temp[0], temp[1] - 1, temp[2] + 1 });
                box[temp[0]][temp[1] - 1] = 1;
                depth = temp[2] + 1;
            }
            if (temp[1] + 1 < M && box[temp[0]][temp[1] + 1] == 0) { // 위
                grownUp.add(new int[] { temp[0], temp[1] + 1, temp[2] + 1 });
                box[temp[0]][temp[1] + 1] = 1;
                depth = temp[2] + 1;
            }
        }
        return depth;
    }
}