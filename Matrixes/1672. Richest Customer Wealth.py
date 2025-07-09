from typing import List 
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        richest_costumer_wealth = 0 #return variable
        
        #Loop for checking and calculating every costumer wealth.
        for costumer in accounts:
            costumer_wealth = 0 #Variable that stores the current client Wealth
            #Loop for checking every b.ank account
            for account in costumer:
                costumer_wealth += account #We add each  accounts money to the total costumer wealth
            
            #We check if this costumer is richer than the current max wealth  we have.
            if costumer_wealth > richest_costumer_wealth:
                richest_costumer_wealth =  costumer_wealth
        
        return richest_costumer_wealth
                
            
            
            
        
        
        
        