class Solution {
    public int[] solution(int[] answers) {
        
        int[] person1 = {1, 2, 3, 4, 5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        int indexForPerson1 = 0;
        int indexForPerson2 = 0;
        int indexForPerson3 = 0;
        int[] answerForPerson = {0,0,0};
        for (int i = 0; i < answers.length; i++, indexForPerson1++, indexForPerson2++, indexForPerson3++) {
            indexForPerson1 = indexForPerson1 % person1.length;
            indexForPerson2 = indexForPerson2 % person2.length;
            indexForPerson3 = indexForPerson3 % person3.length;
            answerForPerson[0] += answers[i] == person1[indexForPerson1] ? 1 : 0;
            answerForPerson[1] += answers[i] == person2[indexForPerson2] ? 1 : 0;
            answerForPerson[2] += answers[i] == person3[indexForPerson3] ? 1 : 0;
        }

        
        int max = -1;
        int[] answerT = new int[3];
        int index = 0;
        for (int i = 0; i < answerForPerson.length; i++) {
            if(max < answerForPerson[i]) {
                max = answerForPerson[i];
                index = 0;
                answerT[index++] = i+1;
            } else if(max == answerForPerson[i]) {
                answerT[index++] = i+1;
            }
        }

        int[] answer = new int[index];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerT[i];
        }
        
        return answer;
    }
}