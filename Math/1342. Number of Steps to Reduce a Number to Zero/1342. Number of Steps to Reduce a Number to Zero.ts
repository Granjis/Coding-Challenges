function numberOfSteps(num: number): number {
    var return_num: number = 0;
    while(num > 0){
        if(num % 2 == 0)
            num /= 2;
        else
            num -= 1;
        return_num ++;
    }
    return return_num;
};