import java.util.Scanner;
import java.util.Stack;

public class boj11559_200202_JJW {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Puyo[][] puyos = new Puyo[12][6];
        String puyoIn = null;
        for (int i = puyos.length - 1; i >= 0; i--) {
            puyoIn = sc.nextLine();
            for (int j = 0; j < puyoIn.length(); j++) {
                if (puyoIn.charAt(j) != '.') {
                    puyos[i][j] = new Puyo(puyoIn.charAt(j), false);
                }
            }
        }

        int answer = 0;
        // printPuyos(puyos);
        while (pangPuyo(puyos) == 1) {
            answer += 1;
            arrangePuyos(puyos);
            printPuyos(puyos);
        }
        System.out.println(answer);
    }

    public static int pangPuyo(Puyo[][] puyos) {
        int isPang = 0;
        Stack<int[]> target = new Stack<>();
        Stack<int[]> tempTarget = new Stack<>();

        // 뿌요뿌요 터지는 대상 확인
        for (int i = 0; i < puyos.length; i++) {
            for (int j = 0; j < puyos[i].length; j++) {
                tempTarget = new Stack<>();
                checkPuyo(puyos, tempTarget, puyos[i][j], i, j);

                // 4개 이상이 모여야 터지는 대상
                if (tempTarget.size() >= 4) {
                    while (tempTarget.empty() == false) {
                        target.push(tempTarget.pop());
                    }
                    isPang = 1; // 터지는 대상인 경우
                }
            }
        }

        // 뿌요뿌요 동시에 터트리기
        while (target.empty() == false) {
            int[] xy = target.pop();
            puyos[xy[0]][xy[1]] = null;
        }

        return isPang;
    }

    public static void checkPuyo(Puyo[][] puyos, Stack<int[]> target, Puyo puyo, int row, int col) {
        if (puyos[row][col] == null) {
            return;
        }

        puyos[row][col].isCheked = true;

        if (row + 1 < puyos.length) {
            if (puyos[row + 1][col] != null && puyos[row + 1][col].isCheked == false
                    && puyos[row + 1][col].color == puyo.color) {
                checkPuyo(puyos, target, puyos[row + 1][col], row + 1, col);
            }
        }

        if (row - 1 >= 0) {
            if (puyos[row - 1][col] != null && puyos[row - 1][col].isCheked == false
                    && puyos[row - 1][col].color == puyo.color) {
                checkPuyo(puyos, target, puyos[row - 1][col], row - 1, col);
            }
        }

        if (col + 1 < puyos[row].length) {
            if (puyos[row][col + 1] != null && puyos[row][col + 1].isCheked == false
                    && puyos[row][col + 1].color == puyo.color) {
                checkPuyo(puyos, target, puyos[row][col + 1], row, col + 1);
            }
        }

        if (col - 1 >= 0) {
            if (puyos[row][col - 1] != null && puyos[row][col - 1].isCheked == false
                    && puyos[row][col - 1].color == puyo.color) {
                checkPuyo(puyos, target, puyos[row][col - 1], row, col - 1);
            }
        }

        int[] xy = { row, col };
        target.push(xy);
    }

    // 뿌요뿌요 정리 및 초기화
    public static void arrangePuyos(Puyo[][] puyos) {
        for (int j = 0; j < puyos[0].length; j++) {
            for (int i = 0; i < puyos.length; i++) {
                if (puyos[i][j] == null) {
                    for (int k = i + 1; k < puyos.length; k++) {
                        if (puyos[k][j] != null) {
                            puyos[i][j] = puyos[k][j];
                            puyos[k][j] = null;
                            break;
                        }
                    }
                }
                if (puyos[i][j] != null) {
                    puyos[i][j].isCheked = false;
                }
            }
        }
    }

    public static void printPuyos(Puyo[][] puyos) {
        System.out.println("=========start=========");
        for (int i = puyos.length - 1; i >= 0; i--) {
            for (int j = 0; j < puyos[i].length; j++) {
                System.out.print(puyos[i][j] == null ? "." : puyos[i][j].color);
            }
            System.out.println();
        }
        System.out.println("==========end=========");
    }

    public static class Puyo {
        public Character color;
        public boolean isCheked;

        public Puyo(Character color, boolean isCheked) {
            this.color = color;
            this.isCheked = isCheked;
        }
    }
}