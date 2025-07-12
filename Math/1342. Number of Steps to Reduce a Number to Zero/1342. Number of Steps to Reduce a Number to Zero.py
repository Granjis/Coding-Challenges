class Solution:
    def numberOfSteps(self, num: int) -> int:

        steps = 0 #Acumulator variable
        
        #Loop for executing the steps to reduce to 0
        while num > 0:
            # Conditional, if num is even we split into 2 else we substract 1 from it
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        
        return steps
        
    
