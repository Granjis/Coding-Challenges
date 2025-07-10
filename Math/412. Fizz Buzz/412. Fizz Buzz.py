from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        #Loop for filling the String's List:
        for num in range(1, n + 1): #We start counting from 1 and have to include number n
            
            if(num % 3 == 0 and num % 5 == 0):
                answer.append("FizzBuzz")
            elif(num % 3 == 0):
                answer.append("Fizz")
            elif(num % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(num))
        return answer
            