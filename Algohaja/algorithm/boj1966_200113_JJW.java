import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class boj1966_200113_JJW {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언

        int testCase = Integer.parseInt(bf.readLine());
        String[] nm, inPriorities, priorities = null;
        String serializedPriorities = null;
        int N, M, priority, cnt = 0;
        Stack<Temp> stack = null;
        Temp temp = null;
        while (testCase > 0) {
            stack = new Stack<>();
            priorities = new String[9];
            cnt = 1;
            nm = bf.readLine().split(" ");
            inPriorities = bf.readLine().split(" ");
            N = Integer.parseInt(nm[0]);
            M = Integer.parseInt(nm[1]);
            for (int i = 0; i < N; i++) {
                priority = Integer.parseInt(inPriorities[i]) - 1;
                if (priorities[priority] == null) {
                    priorities[priority] = inPriorities[i];
                } else {
                    priorities[priority] += inPriorities[i];
                }
                temp = new Temp(inPriorities[i].charAt(0), i);
                stack.push(temp);
            }
            serializedPriorities = getPriorities(priorities);
            while (true) {
                if (stack.peek().left == serializedPriorities.charAt(serializedPriorities.length() - cnt)) {
                    if (stack.peek().right == M) {
                        bw.write(cnt + "\n");
                        break;
                    }
                    stack.pop();
                    cnt++;
                } else {
                    stack.push(stack.pop());
                }
                
            }
            testCase--;
        }
        bw.flush();
        bw.close();
    }

    public static class Temp {
        public Character left;
        public int right;

        public Temp(Character left, int right) {
            this.left = left;
            this.right = right;
        }
    }

    public static String getPriorities(String[] priorities) {
        String output = "";
        for (int i = 0; i < priorities.length; i++) {
            output += priorities[i] == null ? "" : priorities[i];
        }
        return output;
    }
}