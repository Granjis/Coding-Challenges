class Solution {
    public int[] runningSum(int[] nums) {
        int len = nums.length;
        int[] returnList = new int[len];
        int total = 0;
        for(int i = 0; i < len; i++)
        {
            total += nums[i];
            returnList[i] = total;
        } 
        return returnList;
    }
}