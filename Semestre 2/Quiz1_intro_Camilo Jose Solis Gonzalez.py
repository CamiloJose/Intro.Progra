def elimina(num):
    if isinstance(num,int) and num <= 9999 and num > 999:
        if num < 10000 and num > 999:
            dig1 = num %10
            op1= num // 10
            dig2= op1%10
            op2 = op1//10
            dig3=op2%10
            op3=op2//10
            dig4 = op3
            result=dig4,dig3,dig2,dig1
            if dig1 ==0:
                return pop(dig1)
            elif dig2==0:
                return remove(dig1)
            elif dig3==0:
                return remove(dig1)
            elif dig4==0:
                return remove(dig1)
            else: return (dig4*1000)+(dig3*100)+(dig2*10)+dig1
    else: return "Error"
