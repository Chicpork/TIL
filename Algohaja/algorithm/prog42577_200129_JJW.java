class Solution {
    public boolean solution(String[] phone_book) {
        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 0; j < i; j++) {
                if(phone_book[i].length() <= phone_book[j].length()) {
                    if(phone_book[j].startsWith(phone_book[i])) {
                        return false;
                    }
                }
            }
            
            for (int j = i+1; j < phone_book.length; j++) {
                if(phone_book[i].length() <= phone_book[j].length()) {
                    if(phone_book[j].startsWith(phone_book[i])) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}