public class MyMath {

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

    private static void comb(ArrayList<int[]> results, int[] numbers, int[] outputs, int lastIndex, int depth, int r) {
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