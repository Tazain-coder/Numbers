class TerNum:
    def dec2trn(self, dec):
        # this will be the list of characters in the trinary value
        trinary_value = []
        # if the decimal value is 0, then the trinary value is 0
        if dec == 0:
            trinary_value.append(str(0))
        # set test_num to the decimal value
        test_num = int(dec)
        # while test_num is greater than 0
        while test_num > 0:
            # find the remainder of test_num divided by 3
            remainder = test_num%3
            # divide test_num by 3
            test_num = test_num // 3
            # insert the remainder at the beginning of the value list
            trinary_value.insert(0,str(remainder))
        # return the trinary value with "0t" prepended
        if dec < 0:
            return "-0t"+"".join(trinary_value)
        else:
            return "-0t"+"".join(trinary_value)

    def is_ternary(self,num):
        #convert to string
        test_num = str(num)
        #get rid of prefix
        if not test_num.isnumeric():
            test_num = test_num.replace("0t","")
        #test each digit
        for i in test_num:
            if int(i) > 2:
                return False
        return True

    
    def trn2dec(self, trn):
        """
         trn2dec is a function that converts a ternary number to decimal,
         it has one parameter, trn, which is a string containing the ternary number,
         the function returns a decimal number,
         first we define a function to test if the number is ternary,
         the function is_ternary has one parameter, terNum, which is the number we want to test,
         the function returns True if the number is ternary and False if it is not
        """
        def is_ternary(terNum):
            #we convert the number to a string in case it is not
            test_num = str(terNum)
            #if the number is written with the ternary prefix, "0t", we remove it
            if "0t" in test_num:
                test_num = test_num.replace("0t","")
            #we check each digit of the number
            for i in test_num:
                #if any digit is larger than 2, the number is not ternary
                if int(i) > 2:
                    return False
            #if the number is ternary, we return True
            return True
        #we initialize the decimal number as 0
        dec_num = 0
        #we convert the input number to a string in case it is not
        test_num = str(trn)
        #if the number is written with the ternary prefix, "0t", we remove it
        if "0t" in test_num:
            test_num = test_num.replace("0t","")
        #we check if the number is ternary
        if is_ternary(test_num):
            #if it is ternary, we iterate through each digit of the number
            for i,val in enumerate(reversed(test_num)):
                #we convert the digit to an integer and multiply it by 3 raised to the power of the digit's index
                dec_num+=int(val)* 3**i
            #we return the decimal number
            return dec_num
        #if the number is not ternary, we return a message to the user
        else:
            return "Please enter a valid ternary number"
    def all_ternery(self, num_list:list):
        all_trn = False
        for i in num_list:
            if self.is_ternary(i):
                all_trn = True
            else:
                all_trn = False
                break
        return all_trn
        
    def trnAdd(self, num_list:list):
        added = 0
        if self.all_ternery(num_list):
            for nums in num_list:
                added += self.trn2dec(nums)
        return self.dec2trn(added)
    def trnSub(self, num_list:list):
        added = 0
        if self.all_ternery(num_list):
            for nums in num_list:
                added -= self.trn2dec(nums)
        return self.dec2trn(added)
    


