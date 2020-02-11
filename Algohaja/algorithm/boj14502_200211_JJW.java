import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;

public class boj14502_200211_JJW {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] MN = bf.readLine().split(" ");
        String[] temp = null;
        int N = Integer.parseInt(MN[0]);
        int M = Integer.parseInt(MN[1]);
        int[][] map = new int[N][M];
        LinkedList<int[]> virus = new LinkedList<>();
        ArrayList<int[]> blank = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            temp = bf.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
                if (map[i][j] == 2) {
                    virus.add(new int[] { i, j });
                } else if (map[i][j] == 0) {
                    blank.add(new int[] { i, j });
                }
            }
        }
        ArrayList<int[]> comb = MyMath.combination(blank.size(), 3);

        int safeMax = 0;
        int safeMaxTemp = 0;
        int[][] copyMap = null;
        int[] wall1, wall2, wall3;
        int[] combElem;
        LinkedList<int[]> copyVirus = null;

        // Using bfs
        // for (int i = 0; i < comb.size(); i++) {
        // combElem = comb.get(i);
        // wall1 = blank.get(combElem[0] - 1);
        // wall2 = blank.get(combElem[1] - 1);
        // wall3 = blank.get(combElem[2] - 1);

        // map[wall1[0]][wall1[1]] = 1;
        // map[wall2[0]][wall2[1]] = 1;
        // map[wall3[0]][wall3[1]] = 1;

        // copyMap = deepCopy2D(map);
        // copyVirus = new LinkedList<>();
        // for (int[] vi : virus) {
        // copyVirus.add(vi);
        // }
        // safeMaxTemp = bfs(copyMap, copyVirus, N, M);
        // if (safeMaxTemp > safeMax) {
        // safeMax = safeMaxTemp;
        // }

        // map[wall1[0]][wall1[1]] = 0;
        // map[wall2[0]][wall2[1]] = 0;
        // map[wall3[0]][wall3[1]] = 0;
        // }

        // Using bfs
        for (int i = 0; i < comb.size(); i++) {
            combElem = comb.get(i);
            wall1 = blank.get(combElem[0] - 1);
            wall2 = blank.get(combElem[1] - 1);
            wall3 = blank.get(combElem[2] - 1);
            map[wall1[0]][wall1[1]] = 1;
            map[wall2[0]][wall2[1]] = 1;
            map[wall3[0]][wall3[1]] = 1;
            copyMap = deepCopy2D(map);
            for (int[] xy : virus) {
                dfs(copyMap, xy[0], xy[1], N, M);
            }
            safeMaxTemp = checkMap(copyMap);
            if (safeMaxTemp > safeMax) {
                safeMax = safeMaxTemp;
            }
            map[wall1[0]][wall1[1]] = 0;
            map[wall2[0]][wall2[1]] = 0;
            map[wall3[0]][wall3[1]] = 0;
        }

        System.out.println(safeMax);
        // printMap(map);
    }

    public static void printMap(int[][] map) {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int checkMap(int[][] map) {
        int output = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == 0) {
                    output += 1;
                }
            }
        }
        return output;
    }

    public static int[][] deepCopy2D(int[][] original) {
        if (original == null) {
            return null;
        }

        int[][] result = new int[original.length][];
        for (int i = 0; i < original.length; i++) {
            result[i] = Arrays.copyOf(original[i], original[i].length);
        }
        return result;
    }

    public static int bfs(int[][] map, LinkedList<int[]> virus, int N, int M) {
        int[] temp = null;
        while (!virus.isEmpty()) {
            temp = virus.pop();
            if (temp[0] - 1 >= 0 && map[temp[0] - 1][temp[1]] == 0) { // 왼쪽
                virus.add(new int[] { temp[0] - 1, temp[1] });
                map[temp[0] - 1][temp[1]] = 2;
            }
            if (temp[0] + 1 < N && map[temp[0] + 1][temp[1]] == 0) { // 오른쪽
                virus.add(new int[] { temp[0] + 1, temp[1] });
                map[temp[0] + 1][temp[1]] = 2;
            }
            if (temp[1] - 1 >= 0 && map[temp[0]][temp[1] - 1] == 0) { // 아래
                virus.add(new int[] { temp[0], temp[1] - 1 });
                map[temp[0]][temp[1] - 1] = 2;
            }
            if (temp[1] + 1 < M && map[temp[0]][temp[1] + 1] == 0) { // 위
                virus.add(new int[] { temp[0], temp[1] + 1 });
                map[temp[0]][temp[1] + 1] = 2;
            }
        }
        int safe = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == 0) {
                    safe += 1;
                }
            }
        }
        return safe;
    }

    public static void dfs(int[][] map, int x, int y, int N, int M) {
        if (x - 1 >= 0 && map[x - 1][y] == 0) { // 왼쪽
            map[x - 1][y] = 2;
            dfs(map, x - 1, y, N, M);
        }
        if (x + 1 < N && map[x + 1][y] == 0) { // 오른쪽
            map[x + 1][y] = 2;
            dfs(map, x + 1, y, N, M);
        }
        if (y - 1 >= 0 && map[x][y - 1] == 0) { // 아래
            map[x][y - 1] = 2;
            dfs(map, x, y - 1, N, M);
        }
        if (y + 1 < M && map[x][y + 1] == 0) { // 위
            map[x][y + 1] = 2;
            dfs(map, x, y + 1, N, M);
        }
    }

    public static class MyMath {

        public static ArrayList<int[]> combination(int n, int r) {
            int[] numbers = new int[n];
            int[] outputs = new int[r];

            for (int i = 0; i < n; i++) {
                numbers[i] = i + 1;
            }

            int counts = (int) Math.pow(2, r) - 1;
            ArrayList<int[]> results = new ArrayList<>(counts);

            // combAll(results, numbers, outputs, 0, 0, r);
            comb(results, numbers, outputs, 0, 0, r);
            return results;
        }

        public static ArrayList<int[]> combination(int[] numbers, int r) {
            if (numbers.length < r) {
                return null;
            }
            int[] outputs = new int[r];

            int counts = (int) Math.pow(2, r) - 1;
            ArrayList<int[]> results = new ArrayList<>(counts);

            // combAll(results, numbers, outputs, 0, 0, r);
            comb(results, numbers, outputs, 0, 0, r);
            return results;
        }

        private static void comb(ArrayList<int[]> results, int[] numbers, int[] outputs, int lastIndex, int depth,
                int r) {
            if (depth == r) {
                results.add(outputs.clone());
                return;
            }

            for (int i = lastIndex; i < numbers.length; i++) {
                outputs[depth] = numbers[i];
                comb(results, numbers, outputs, i + 1, depth + 1, r);
                outputs[depth] = 0;
            }
        }

        private static void combAll(ArrayList<int[]> results, int[] numbers, int[] outputs, int lastIndex, int depth,
                int r) {
            if (depth == r) {
                return;
            }

            int[] tempOutputs = null;
            for (int i = lastIndex; i < numbers.length; i++) {
                tempOutputs = outputs.clone();
                tempOutputs[depth] = numbers[i];
                results.add(tempOutputs);
                combAll(results, numbers, tempOutputs, i + 1, depth + 1, r);
            }
        }

        public static ArrayList<int[]> permutation(int n, int r) {
            int[] numbers = new int[n];
            int[] outputs = new int[r];
            boolean[] isVisited = new boolean[n];

            int counts = 1;
            for (int i = 0; i < n; i++) {
                numbers[i] = i + 1;
                counts *= i + 1;
            }

            ArrayList<int[]> results = new ArrayList<>(counts);

            perm(results, numbers, outputs, isVisited, 0, n, r);
            return results;
        }

        public static ArrayList<int[]> permutation(int[] numbers, int r) {
            int[] outputs = new int[r];
            boolean[] isVisited = new boolean[numbers.length];

            int counts = 1;
            for (int i = 0; i < numbers.length; i++) {
                counts *= i + 1;
            }

            ArrayList<int[]> results = new ArrayList<>(counts);

            perm(results, numbers, outputs, isVisited, 0, numbers.length, r);
            return results;
        }

        private static void perm(ArrayList<int[]> results, int[] numbers, int[] outputs, boolean[] isVisited, int depth,
                int n, int r) {
            if (depth == r) {
                results.add(outputs.clone());
                return;
            }

            for (int i = 0; i < numbers.length; i++) {
                if (!isVisited[i]) {
                    isVisited[i] = true;
                    outputs[depth] = numbers[i];
                    perm(results, numbers, outputs, isVisited, depth + 1, n, r);
                    isVisited[i] = false;
                }
            }
        }
    }
}