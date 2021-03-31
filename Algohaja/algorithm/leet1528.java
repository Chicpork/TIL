import javax.xml.stream.events.Characters;

/**
 * leet1528
 */
public class leet1528 {

    public static void main(String[] args) {
        String s = "codeleet";
        int[] indices = {4,5,6,7,0,2,1,3};
        char[] s2 = new char[indices.length];

        for (int i = 0; i < indices.length; i++) {
            s2[indices[i]] = s.charAt(i);
        }
        StringBuilder sb = new StringBuilder();
        return sb.append(s2);
    }
}