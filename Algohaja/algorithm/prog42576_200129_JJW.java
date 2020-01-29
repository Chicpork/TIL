import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        int index = -1;
        for (int i = 0; i < completion.length; i++) {
            if(!participant[i].equals(completion[i])) {
                index = i;
                break;
            }
        }

        return index == -1 ? participant[participant.length-1] : participant[index];
    }
}