import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class boj1966_200113_JJW {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); 
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int testCase = Integer.parseInt(bf.readLine());
        String[] nm, inPriorities = null;
        List<Integer> priorities = null;
        int N, M, priority, cnt = 0;
        Queue<int[]> queue = null;
        for (int j = 0; j < testCase; j++) {
            queue = new LinkedList<>();
            priorities = new ArrayList<>();
            cnt = 1;
            nm = bf.readLine().split(" ");
            inPriorities = bf.readLine().split(" ");
            
            N = Integer.parseInt(nm[0]);
            M = Integer.parseInt(nm[1]);
            for (int i = 0; i < N; i++) {
                priority = Integer.parseInt(inPriorities[i]);
                priorities.add(priority);
                int[] temp = {i, priority};
                queue.add(temp);
            }
            
            priorities.sort(Comparator.reverseOrder());

            while (true) {
                if (queue.peek()[1] == priorities.get(0)) {
                    if (queue.peek()[0] == M) {
                        bw.write(cnt + "\n");
                        break;
                    }
                    queue.poll();
                    priorities.remove(0);
                    cnt++;
                } else {
                    queue.add(queue.poll());
                }
            }
        }
        bw.flush();
        bw.close();
    }
}