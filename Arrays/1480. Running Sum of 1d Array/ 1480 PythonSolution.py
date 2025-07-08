from typing import List
class Solution:
    def runningSumV1(self, nums: List[int]) -> List[int]:
    
        return_list = []
        

        #We iterate all over the list:
        for i in range(len(nums)):
            current_number = nums[i]
            if i == 0:
                return_list.append(current_number)
            else:
                return_list.append(current_number + return_list[i-1])
            
                

        return return_list


    #Using recursion
    def runningSum3(self, nums: list[int]) -> list[int]:
      
        if len(nums) <= 1: #Checks that we are not trying to execute the code on an single element list
            return_list = [nums[-1]]
            return return_list

      
        return_list = self.runningSum(nums[:-1])
        last_number = nums[-1] + return_list[-1]
        return_list.append(last_number)
     
        return return_list

    #Winner by far
    def runningSum1(self, nums: List[int]) -> List[int]:
            
        total = 0
        return_list = []

        for i in range(len(nums)):
     
            total += nums[i]
            return_list.append(total)

        return return_list