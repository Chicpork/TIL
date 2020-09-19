import java.util.LinkedList;
import java.util.Queue;

public class problem3 {
    public static void main(String[] args) {
        
        String[] info = {"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
        String[] query = {"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};

        int condiNum = 4;
        int score, idx;
        int[] answer = new int[query.length];
        String[] condisT = null;
        String[] infoT = null;
        char[][] condis = new char[query.length][];
        int[] scores = new int[query.length];

        boolean pass = true;
        for (int i = 0; i < query.length; i++) {
            condis[i] = new char[condiNum];
            score = -1;
            idx = 0;

            condisT = query[i].split(" ");

            for (int j = 0; j < condisT.length-1; j+=2) {
                condis[i][idx++] = condisT[j].charAt(0);
            }
            scores[i] = Integer.parseInt(condisT[condisT.length-1]);
        }

        for (int i = 0; i < info.length; i++) {
            infoT = info[i].split(" ");
            score = Integer.parseInt(infoT[infoT.length-1]);

            for (int j = 0; j < condis.length; j++) {
                pass = true;
                if (score < scores[j]) {
                    pass = false;
                    continue;
                }

                for (int j2 = 0; j2 < infoT.length-1; j2++) {
                    if (!(condis[j][j2] == '-') && !(infoT[j2].charAt(0) == condis[j][j2])) {
                        pass = false;
                        break;
                    }
                }
                if (pass) {
                    answer[j]++;
                }
            }
        }
        for (int i : answer) {
            System.out.print (i + " ");
        }
    }
}
