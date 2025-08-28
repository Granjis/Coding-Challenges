
class Solution {
    public String longestCommonPrefix(String[] strs) {
       
        String prefix = strs[0];
        if(prefix == "") return "";

        for(int i = 1; i < strs.length; i++){

            String currentWord = strs[i];
            if(currentWord == "") return "";

            boolean found = false;
            int prefixLenght = prefix.length();
            int currentWordLenght = currentWord.length();
            int currentlenght = prefixLenght < currentWordLenght ? prefixLenght : currentWordLenght;
            int index = 0;
            while(!found){
                
                if(index == currentlenght) return "";

                String currentSubPrefix = prefix.substring(0, currentlenght - index);
               
                
                if(currentSubPrefix.equals(currentWord.substring(0, currentlenght - index))){
                    prefix = currentSubPrefix;
                    found = true;
                    }
                index ++;
            }
            
        }
        return prefix;
    }
}