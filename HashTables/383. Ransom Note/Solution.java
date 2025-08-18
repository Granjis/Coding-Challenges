import java.util.HashMap;
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

    HashMap<String,Integer> magazineHashMap = new HashMap<>();
    
    for(int i = 0; i < magazine.length(); i ++){
        char charActual = magazine.charAt(i);
        magazineHashMap.put(charActual, magazineHashMap.getOrDefault(charActual,0) + 1);
    }

    for(int j = 0; j < ransomNote.length(); j ++){
        Char charActual = ransomNote.charAt(j);
        if(magazineHashMap.getOrDefault(charActual, 0) <= 0)
            return false;
        magazineHashMap.put(magazine, magazineHashMap.get(charActual) + 1);
    }
    return true; 
        
    }
}