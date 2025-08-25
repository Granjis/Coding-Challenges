from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        if "" in strs:
            return ""
        
        prefix = strs[0]
        #We run trought all the words in the list.
        for word in strs[1:]:
            
            word_length = len(word)
            prefix_length = len(prefix)
            current_initial = prefix[0]
            #We check that the current prefix and the current word have the initial letter in common
            if current_initial != word[0]:
                return ""
            #We check that the current prefix or the current word have more than one letter.
            elif prefix_length == 1 or word_length == 1:
                prefix = current_initial
            else:
                local_prefix = current_initial
                iterations = prefix_length if len(prefix) > word_length else word_length
                found = False
                index = 1
                while index < iterations + 1 and not found:
                    
                    print("current prefix:", prefix[:index])
                    print("current word:", word[:index])
                    if prefix[:index] != word[:index]:
                        prefix = local_prefix
                        found = True
                    
                    else:
                        local_prefix = word[:index]
                        index += 1 
                        
        return prefix
        
        
        
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        
        current_prefix = strs[0]
        
        for word in strs[1:]:
            
            found = False
            index = 0
            while not found:
                
               
                longer_word = current_prefix if len(current_prefix) > len(word) else word
                local_prefix = longer_word[:len(longer_word) - index]
                
                if local_prefix not in word:
                    if index == len(current_prefix):
                        return ""
                    index += 1  
                    
                else:   
                    current_prefix = local_prefix     
                    found = True
        
        return current_prefix
    
    #Fastest by far 
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        
        if "" in strs:
            return ""
        
        prefix = strs[0]
        
        for word in strs[1:]:
            
            found = False
            index = 0
            prefix_len = len(prefix)
            while not found:

                current_index = prefix_len - index
                if prefix[:current_index] != word[:current_index]:
                    index += 1
                    if index > prefix_len:
                        return ""
                else:
                    found = True
                    prefix = prefix[:current_index]
                
        return prefix
                
                
                
                
                
            
            
    
            
            
    