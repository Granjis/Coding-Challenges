package Matrixes;

class Solution{
    public int maximumWealth(int[][] accounts) {

        int maximumWealth = 0;
        int numberOfAccounts = accounts[0].length;
        for(int costumer = 0; costumer <  accounts.length; costumer ++){
            int costumerWealth = 0;
            for(int account = 0; account < numberOfAccounts; account ++)
            {
                costumerWealth += accounts[costumer][account];
            }

            if(costumerWealth > maximumWealth)
                maximumWealth = costumerWealth;
        }

        return maximumWealth;
        
    }
}