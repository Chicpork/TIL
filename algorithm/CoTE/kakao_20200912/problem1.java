public class problem1 {
    public static void main(String[] args) {
        String answer = new_id;

        // step1
        answer = answer.toLowerCase();
        
        // step2
        String regExp = "[^a-z0-9-_\\.]*";
        answer = answer.replaceAll(regExp, "");

        // step3
        while (answer.contains("..")) {
            answer = answer.replaceAll("\\.\\.", ".");
        }

        // step4
        while (answer.length() != 0 && answer.charAt(0) == '.') {
            answer = answer.substring(1, answer.length());
        }
        while (answer.length() != 0 && answer.charAt(answer.length()-1) == '.') {
            answer = answer.substring(0, answer.length()-1);
        }

        // step5
        if (answer.length() == 0) {
            answer = "a";
        }

        // step6
        if (answer.length() >= 16) {
            answer = answer.substring(0, 15);
            while (answer.length() != 0 && answer.charAt(answer.length()-1) == '.') {
                answer = answer.substring(0, answer.length()-1);
            }
        }

        // step7
        while (answer.length() <= 2) {
            answer = answer + answer.charAt(answer.length()-1);
        }
    }
}
