class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        #We create a hashtable(Dictionaries) for every function's argument. The keys are going to be the different caracthers
        ramsomNoteHashTable = {}
        magazineHashTable = {}
        
        #Now we run trough the strings counting the ocurrences of every letter on both ransomNote and magazine.
        for char in ransomNote:
            #If the char is already in the dictionary we add 1 to the counter, else we create the enty an the value is 1.
            if char in ramsomNoteHashTable:
                ramsomNoteHashTable[char] += 1
            else:
                ramsomNoteHashTable[char] = 1
        
        for char in magazine:
            #If the char is already in the dictionary we add 1 to the counter, else we create the enty an the value is 1.
            if char in magazineHashTable:
                magazineHashTable[char] += 1
            else:
                magazineHashTable[char] = 1
                
        #Now we check that for every letter in ransomNote we have enought of it on magazine.
        for key in list(ramsomNoteHashTable.keys()):
            
            #We get the amount of ocurrences of the char on both dictionaries, if the letters is not on magazine or there are less of them,
            #It returns False
            if magazineHashTable.get(key, 0) < ramsomNoteHashTable[key]:
                return False
            
        return True 
                 
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        
        magazine_hash = {}
        
        for char in magazine:
            magazine_hash[char] = magazine_hash.get(char, 0) + 1
        
        for char in ransomNote:
            
            if magazine_hash.get(char, 0) <= 0:
                return False

            magazine_hash[char] -= 1
           
        
        return True
        
    #WINNER, best running time. It only checks every letter once. 
    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        
        #set(ransomNote) returns a set of every letter in the string.
        for char in set(ransomNote):
            
            if ransomNote.count(char) > magazine.count(char):
                return False
        
        return True 
        
        
            
        