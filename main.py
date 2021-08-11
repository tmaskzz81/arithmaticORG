# this program is not for CHEATING purpose
# this code is open source
# best of luck .. tmask

import math
import time

def get_unsigned_maxValue(n):
    n = int(n)
    return str(pow(2, n) - 1)

def get_unsigned_minValue(n):
    return "0"

def get_signed_maxValue(n):
    n = int(n)
    return str("+" + str(pow(2, n-1) - 1))

def get_signed_minValue(n):
    n = int(n)
    return str("-" + str(pow(2, n-1) - 1))

def get_unsigned_in_nbits(deciNumber,n):
    biNumber = get_unsigned_magnitude(deciNumber)
    addBits = int(n) - len(biNumber)
    result =  ("0" * addBits) + biNumber
    return result

def print_value_in_nbits(deciNumber, n):
    if int(deciNumber) > 0:
        biNumber = get_signed_magnitude(deciNumber)
        addBits = int(n) - len(biNumber)
        result =  ("0" * addBits) + biNumber
        print(deciNumber + " IN SIGNED REPRESENTATION IN " + str(n) + " BITS IS : " + result)
        print(deciNumber + " IN 2'sCOMPLIMENT REPRESENTATION IN " + str(n) + " BITS IS : " + result)

    elif int(deciNumber) < 0:
        # signed representation
        biNumber = get_signed_magnitude(deciNumber)[1:]
        addBits = int(n) - len(biNumber) -1
        result =  ("0" * addBits) + biNumber
        result = "1" + result
        print(deciNumber + " IN SIGNED REPRESENTATION IN " + str(n) + " BITS IS : " + result)
        
        # 2's compliment representation
        biNumber = twos_compliment_process(deciNumber)
        addBits = int(n) - len(biNumber)
        result =  ("1" * addBits) + biNumber
        print(deciNumber + " IN 2'sCOMPLIMENT REPRESENTATION IN " + str(n) + " BITS IS : " + result)
        
def get_twos_compliment_maxValue(n):
    n = int(n)
    return str("+" + str(pow(2, n-1) - 1))

def get_twos_compliment_minValue(n):
    n = int(n)
    return str("-" + str(pow(2, n-1)))

def print_minimum_bits_to_represent(deciNumber):
    print("SIGNED MAGNITUDE : " + str(len(get_signed_magnitude(deciNumber))) + " BITS")
    print("2's COMPLIMENT : " + str(len(twos_compliment_process(deciNumber))) + " BITS")

def get_unsigned_value(biNumber):
    result = 0
    temp = int(biNumber)
    for i in range(len(str(biNumber))):
        result = result + ((temp % 10) * (2 ** i))
        temp = temp // 10
    result = str(result)
    return result

def get_signed_value(biNumber):
    result = 0
    temp = int(biNumber)

    for i in range(len(str(biNumber)) - 1):
        result = result + ((temp % 10) * (2 ** i))
        temp = temp // 10

    sign = temp
    if sign == 1:
        result = -1 * result

    return str(result)

def get_unsigned_magnitude(deciNumber):
    deciNumber = int(deciNumber)
    if deciNumber < 0:
        deciNumber = deciNumber * -1

    result = ""
    temp = deciNumber
    while temp != 0:
        result = str(temp % 2) + result
        temp = temp // 2

    return result

def get_signed_magnitude(deciNumber):
    biNumber = get_unsigned_magnitude(deciNumber)
    deciNumber = int(deciNumber)
    result = ""

    if deciNumber < 0:
        result = "1" + biNumber
    elif deciNumber > 0:
        result = "0" + biNumber

    return result

def sum_binary_nums(x,y):
        max_len = max(len(x), len(y))

        x = x.zfill(max_len)
        y = y.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry !=0 : result = '1' + result

        return result.zfill(max_len)

def twos_compliment_process(deciNumber):
    deciNumber = int(deciNumber)
    if deciNumber > 0:
        return get_signed_magnitude(deciNumber)

    elif deciNumber < 0:
        i = 0
        while True:
            if (deciNumber / (2 ** i)) == -1.0:
                return get_unsigned_magnitude(deciNumber)

            if 2 ** i > abs(deciNumber):
                break

            i = i + 1

        result = ""
        temp = int(get_signed_magnitude(-1 * deciNumber))
        for i in range(len(str(temp))):
            t = temp % 10
            temp = temp // 10
            if t == 0:
                result = "1" + result
            elif t == 1:
                result = "0" + result

        result = "1" + result
        result = sum_binary_nums(result, "1")

        return result

def two2two(number):
    result=""
    flag = False
    for i in range(len(number) - 1,-1,-1):
        if flag == False:
            if number[i] == "1":
                flag = True
            result = number[i] + result

        else:
            if number[i] == "0":
                result = "1" + result
            elif number[i] == "1":
                result = "0" + result
    return result

def twos_compliment_value(biNumber):
    if int(get_signed_value(biNumber)) > 0:
        return get_signed_value(biNumber)

    elif int(get_signed_value(biNumber)) <= 0:
        result = ""
        temp = int(biNumber)
        for i in range(len(str(temp))):
                t = temp % 10
                temp = temp // 10
                if t == 0:
                    result = "1" + result
                elif t == 1:
                    result = "0" + result

        r = sum_binary_nums(result, "1")
        result = get_unsigned_value(int(r))
        return "-" + result

def detailed_result(number):
    if number < 0:
        number = -1 * number

    result = ""
    temp = number
    while temp != 0:
        print(str(temp) + " / " + "2 = " + str(temp // 2) + " with remainder " + str(temp % 2))
        result = str(temp % 2) + result
        temp = temp // 2
    print("number %s converted to unsigned magnitude is therefore equal to : " % number)
    print(result)

def deciToBi(number):
    print()
    print("### DECIMAL TO BINARY ###")
    print("the input : " + str(number))
    print("unsigned magnitude : " + get_unsigned_magnitude(number))
    print("signed magnitude : " + get_signed_magnitude(number))
    print("2s compliment : " + twos_compliment_process(number))
    print()
    print("*" * 50)

def biToDeci(number):
    print()
    print("### BINARY TO DECIMAL ###")
    print("the input : " + str(number))
    print("unsigned magnitude : " + get_unsigned_value(number))
    print("signed magnitude : " + get_signed_value(number))
    print("2s compliment : " + str(twos_compliment_value(number)))
    print()
    print("*" * 50)

def print_sum(num1, num2):
    # Variables
    max_len = max(len(num1), len(num2))
    overflow = False
    decinum1 = twos_compliment_value(num1)
    decinum2 = twos_compliment_value(num2)
    result = sum_binary_nums(num1,num2)

    # Process for overflow
    # check if it carry or not
    # test : the decimal value of result
    if max_len == len(sum_binary_nums(num1,num2)):
        deciresult = twos_compliment_value(result)
        carry  = False
    else:
        deciresult = twos_compliment_value(result[1:])
        carry = result[0]
        result = result[1:]

    if int(decinum1) + int(decinum2) != int(deciresult):
        overflow = True

    # start print
    print()
    print("### PRINT SUMMATION ###")
    print("NUM1 : " + num1 + "\t(" + decinum1 + ")" )
    print("NUM2 : " + num2 + "\t(" + decinum2 + ")" )
    print("THE RESULT : " + result + "\t(" + deciresult + ")")
    print("CARRY : " + str(carry))
    print("OVERFLOW : " + str(overflow))
    print("ERROR IN THE RESULT : " + str(overflow))
    print()
    print("*" * 75)

def print_sub(num1,num2):
    print("\n### PRINT SUBTRACTION ###")
    print(num2 + " >>> ", end=" ")
    num2 = two2two(num2)
    print(num2)
    print_sum(num1, num2)

def LSHR(C,A):
    return C + A[:len(A) - 1]

def unsigned_multi(M,Q):
    print()
    print("IN DECIMAL : ")
    MM = int(get_unsigned_value(M))
    QQ = int(get_unsigned_value(Q))
    print("M = " + str(MM))
    print("Q = " + str(QQ))
    print("M * Q = " + str(MM*QQ))
    print()

    max_len = int(max(len(M),len(Q)))
    A = "0" * max_len
    C = "0"
    countAdd = 0
    countShift = 0
    print("C" + "\t" + "A" + "\t" + "Q" + "\t" + "M")
    print(C + "\t" + A + "\t" + Q + "\t" + M)
    print("--------------------------------------------------")

    for i in range(max_len):
        if Q[len(Q)-1] == "1":
            A = sum_binary_nums(M,A)
            if len(A) == max_len:
                C = "0"
            else:
                C = A[0]
                A = A[1:]
            countAdd = countAdd + 1
            print(C + "\t" + A + "\t" + Q + "\t" + M  + "\tADD")


        Q = LSHR(A[len(A) - 1],Q)
        A = A[:len(A) - 1]
        A = C + A
        C = "0"
        countShift = countShift + 1
        print(C + "\t" + A + "\t" + Q + "\t" + M  + "\tSHIFT")
        print()

    print("THE RESULT : " + A + Q)
    print("IN THE DECIMAL : " + get_unsigned_value(A + Q))
    print("# OF SHIFT : " + str(countShift))
    print("# OF ADD : " + str(countAdd))

def ASHR(A):
    A = A[:len(A)-1]
    A = A[0] + A
    return A

def boothAlgorithm(M,Q):
    print()
    print("IN DECIMAL : ")
    MM = int(twos_compliment_value(M))
    QQ = int(twos_compliment_value(Q))
    print("M = " + str(MM))
    print("Q = " + str(QQ))
    print("M * Q = " + str(MM*QQ))
    print()
    max_len = int(max(len(M),len(Q)))
    countShift = 0
    countSum = 0
    countSub = 0
    Q_1 = "0"
    Q0 = Q[len(Q) - 1]
    A = "0" * max_len
    print("A" + "\t" + "Q" + "\t" + "Q-1" + "\t" + "M")
    print(A + "\t" + Q + "\t" + Q_1 + "\t" + M)
    print("----------------------------------------------------")

    for i in range(max(len(M),len(Q))):
        if Q0 == "1" and Q_1 == "0":
            A = sum_binary_nums(A,two2two(M)) # A - M
            if len(A) > max_len:
                A = A[1:]
            countSub = countSub + 1
            print(A + "\t" + Q + "\t" + Q_1 + "\t" + M + "\t" + "A - M")

        elif Q0 == "0" and Q_1 == "1":
            A = sum_binary_nums(A,M) # A + M
            if len(A) > max_len:
                A = A[1:]
            countSum = countSum + 1
            print(A + "\t" + Q + "\t" + Q_1 + "\t" + M + "\t" + "A + M")

        Q_1 = Q0
        Q = Q[:len(Q) - 1]
        Q = A[len(A) - 1] + Q
        A = ASHR(A)
        Q0 = Q[len(Q) - 1]
        countShift = countShift + 1
        print(A + "\t" + Q + "\t" + Q_1 + "\t" + M + "\t" + "Shift")
        print()


    result = A + Q
    print("THE RESULT : " + result)
    print("IN THE DECIMAL : " + twos_compliment_value(result))
    print("# OF SHIFT : " + str(countShift))
    print("# OF ADD : " + str(countSum))
    print("# OF SUBTRACTION : " + str(countSub))

def fractionToDeciProcess(number):
    i = 0
    inte = ""
    flote = ""
    while number[i] != ".":
        inte += number[i]
        i += 1
    i += 1
    for j in range(i,len(number)):
        flote += number[j]
    inte = get_unsigned_value(inte)

    result = int(inte)
    j = 1
    for i in range(len(flote)):
        result += float(flote[i]) / (2) ** j
        j += 1
    return str(result)

def fractionToDeci(number):
    print()
    result = fractionToDeciProcess(number)

    print(number + " >>> " + str(result))
    print()
    print("*" * 75)

def deciToFractionProcess(deciNumber):
    i = 0
    inte = ""
    flote = "0"
    while deciNumber[i] != ".":
        inte += deciNumber[i]
        i += 1

    result = get_unsigned_magnitude(inte) + "."

    for j in range(i,len(deciNumber)):
        flote += deciNumber[j]

    flote = float(flote)
    r = ""
    t = flote
    for i in range(5):
        t = t * 2
        s = int(t)
        r += str(s)
        t = t - s
    result += r
    return str(result) 

def deciToFraction(deciNumber):
    print()
    result = deciToFractionProcess(deciNumber)

    print(deciNumber + " >>> " + result)
    print()
    print("*" * 75)

def program(): 
    print("HI ... ")
    time.sleep(1)

    print("1  : DECIMAL NUMBER TO BINARY.")
    print("2  : BINARY NUMBER TO DECIMAL.")
    print("3  : THE MAXIMUM AND MINIMUM VALURE IN N BITS IN UNSIGNED REPRESENTATION.")
    print("4  : THE MAXIMUM AND MINIMUM VALURE IN N BITS IN SIGNED REPRESENTATION.")
    print("5  : THE MAXIMUM AND MINIMUM VALURE IN N BITS IN 2'S COMPLIMENT REPRESENTATION.")
    print("6  : 2's COMPLIMENT OF BINARY VALUE.")
    print("7  : SUMMATION (BINARY NUMBER INPUT).")
    print("8  : UNSIGNED MULTIPICATION.")
    print("9  : BOOTH ALGORITHM.")
    print("10 : FLOATING POINT BINARY TO DECIMAL.")
    print("11 : FLOATING POINT DECIMAL TO BINARY.")
    print("12 : FLOATING POINT FORMAT TO DECIMAL, BINARY VALUE.")
    print("13 : DECIMAL, BINARY VALUE TO FLOATIONG POINT FORMAT.")
    print("14 : IEEE 754.")
    print("15 : ARITHMATIC SHIFT RIGHT.")
    print("16 : SUBTRACTION (BINARY NUMBER INPUT).")
    print("17 : DECIMAL TO BINARY IN N BITS.")
    print("Q  : quit.")
    
    while True:
        print("PLEASE ENTER YOUR NEEDS : ", end = "")
        menuInput = input()
        print()
        print()

        if menuInput == "1":
            print("### DECIMAL NUMBER TO BINARY.")
            valueInput = input("ENTER THE DECIMAL VALUE : ")
            deciToBi(valueInput)

        elif menuInput == "2":
            print("### BINARY NUMBER TO DECIMAL.")
            valueInput = input("ENTER THE BINARY VALUE : ")
            biToDeci(valueInput)

        elif menuInput == "3":
            print("### THE MAXIMUM AND MINIMUM VALURE IN N BITS IN UNSIGNED REPRESENTATION.")
            valueInput = input("HOW MANY BITS THE BINARY NUMBER HAVE? : ")
            print("\nTHE MINIMUN DECINAL VALUE IN UNSIGNED REPRESENTAION IS : " 
            + get_unsigned_minValue(valueInput))
            print("AND ... ")
            print("THE MAXIMUM DECINAL VALUE IN UNSIGNED REPRESENTAION IS : " 
            + get_unsigned_maxValue(valueInput) + " >>> (2^" + valueInput + " - 1)")

        elif menuInput == "4":
            print("### THE MAXIMUM AND MINIMUM VALURE IN N BITS IN SIGNED REPRESENTATION.")
            valueInput = input("HOW MANY BITS THE BINARY NUMBER HAVE? : ")
            print("\nTHE MINIMUN DECINAL VALUE IN SIGNED REPRESENTAION IS : " 
            + get_signed_minValue(valueInput) + " >>> (-2^" + str(int(valueInput) - 1) + " - 1)")
            print("AND ... ")
            print("THE MAXIMUM DECINAL VALUE IN SIGNED REPRESENTAION IS : " 
            + get_signed_maxValue(valueInput) + " >>> (+2^" + str(int(valueInput) - 1) + " - 1)")

        elif menuInput == "5":
            print("### THE MAXIMUM AND MINIMUM VALURE IN N BITS IN 2'S COMPLIMENT REPRESENTATION.")
            valueInput = input("HOW MANY BITS THE BINARY NUMBER HAVE? : ")
            print("\nTHE MINIMUN DECINAL VALUE IN 2's COMPLIMENT REPRESENTAION IS : " 
            + get_twos_compliment_minValue(valueInput) + " >>> (-2^" + str(int(valueInput) - 1) + " )")
            print("AND ... ")
            print("THE MAXIMUM DECINAL VALUE IN 2's COMPLIMENT REPRESENTAION IS : " 
            + get_twos_compliment_maxValue(valueInput) + " >>> (+2^" + str(int(valueInput) - 1) + " - 1)")

        elif menuInput == "6":
            print("### 2's COMPLIMENT OF BINARY VALUE.")
            valueInput = input("ENTER THE BINARY VALUE : ")
            print("THE 2's COMPLIMENT OF " + valueInput + " IS : " + two2two(valueInput))

        elif menuInput == "7":
            print("### SUMMATION (BINARY NUMBER INPUT).")
            num1 = input("ENTER THE FIRST VALUE : ")
            num2 = input("ENTER THE SECOND VALUE : ")
            print_sum(num1, num2)

        elif menuInput == "8":
            print("### UNSIGNED MULTIPICATION.")
            M = input("ENTER THE VALUE OF M (MULTIPLICAND): ")
            Q = input("ENTER THE VALUE OF Q (MULTIPLIER): ")
            unsigned_multi(M,Q)

        elif menuInput == "9":
            print("### BOOTH ALGORITHM.")
            M = input("ENTER THE VALUE OF M (MULTIPLICAND): ")
            Q = input("ENTER THE VALUE OF Q (MULTIPLIER): ")
            boothAlgorithm(M,Q)

        elif menuInput == "10":
            print("### FLOATING POINT BINARY TO DECIMAL.")
            valueInput = input("ENTER THE FRACTION VALUE : ")
            fractionToDeci(valueInput)

        elif menuInput == "11":
            print("### FLOATING POINT DECIMAL TO BINARY.")
            valueInput = input("ENTER THE DECIMAL VALUE : ")
            deciToFraction(valueInput)

        elif menuInput == "12":
            print("### FLOATIONG POINT FORMAT TO DECIMAL, BINARY VALUE : ")
            floating_point_format_value()
        
        elif menuInput == "13":
            print("###  DECIMAL, BINARY VALUE TO FLOATIONG POINT FORMAT : ")
            floating_point_format()

        elif menuInput == "14":
            print("### IEEE 754 : ")
            print("s : sigle format.")
            print("d : double format.")
            x = input(">>> ")
            if x == "s":
                allBits = "32"
                biasBits = "8"
                fractionBits = "23"

            else:
                allBits = "64"
                biasBits = "11"
                fractionBits = "52"
            
            ieee754_value(allBits, biasBits, fractionBits)
        
        elif menuInput == "15":
            print("### ARITHMATIC SHIFT RIGHT : ")
            x = input("ENTER THE BINATY NUMBER : ")
            print(" >>>>>  "  + ASHR(x))

        elif menuInput == "16":
            print("### SUBTRACTION (BINARY NUMBER INPUT).")
            num1 = input("ENTER THE FIRST VALUE : ")
            num2 = input("ENTER THE SECOND VALUE : ")
            print_sub(num1, num2)

        elif menuInput == "17":
            print("### DECIMAL TO BINARY IN N BITS.")
            number = input("ENTER THE DECIMAL NUMBER : ")
            n = input("ENTER THE NUMBER OF BITS : ")
            print_value_in_nbits(number, n)

        elif menuInput.upper() == "Q":
            print("*" * 75)
            print("*" * 75)
            print("THE END. THE END. THE END.")
            print("*" * 75)
            print("*" * 75)
            break
        
        else:
            print("error in the request".upper())
        print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
        print()

def ieee754_value(allBits, biasBits, fractionBits):
    sign = input("ENTER THE SIGN (0,1) : ")
    BEBi = input("ENTER THE BIAS EXPONANT : ")
    fraction = input("ENTER THE FRACTION : ")

    # addBits = int(fractionBits) - len(fraction)
    # if len(fraction) < int(fractionBits):
    #     fraction = fraction + ("0" * addBits)

    print("\n" + sign + "|" + BEBi + "|" + fraction, end="\n\n")
    BE = get_unsigned_value(BEBi)
    bias = pow(2, int(biasBits)-1) - 1
    E = int(BE) - bias
    
    unnormalizedNumber = float("1." + fraction)

    if E > 0:
        for i in range(E):
            unnormalizedNumber = unnormalizedNumber * 10
    else:
        for i in range(abs(E)):
            unnormalizedNumber = unnormalizedNumber / 10
    
    unnormalizedNumber = str(unnormalizedNumber)
    if sign == '1':
        sign = '-'
    elif sign == '0':
        sign = '+'
        
    print("E : " + str(E))
    print("bias : " + str(bias))
    print("BE : " + str(BE))
    print("THE RESULT IN BINARY IS : " + sign + unnormalizedNumber)
    result = sign + fractionToDeciProcess(unnormalizedNumber)
    print("THE RESULT IN DECIMAL IS : " + result)

def floating_point_format_value():
    sign = input("ENTER THE SIGN (0,1) : ")
    BEBi = input("ENTER THE BIAS EXPONANT : ")
    fraction = input("ENTER THE FRACTION : ")
    print("\n" + sign + "|" + BEBi + "|" + fraction, end="\n\n")
    biasBits = len(BEBi)
    fractionBits = len(fraction)
    allBits =  biasBits + fractionBits + len(sign)

    BE = get_unsigned_value(BEBi)
    bias = pow(2, int(biasBits)-1) - 1
    E = int(BE) - bias

    unnormalizedNumber = float("1." + fraction)
    
    if E > 0:
        for i in range(E):
            unnormalizedNumber = unnormalizedNumber * 10
    else:
        for i in range(abs(E)):
            unnormalizedNumber = unnormalizedNumber / 10
    unnormalizedNumber = str(unnormalizedNumber)

    if sign == '1':
        sign = '-'
    elif sign == '0':
        sign = '+'
    
    print("E : " + str(E))
    print("bias : " + str(bias))
    print("BE : " + str(BE))
    print("THE RESULT IN BINARY IS : " + sign + unnormalizedNumber)
    result = sign + fractionToDeciProcess(unnormalizedNumber)
    print("THE RESULT IN DECIMAL IS : " + result)

def floating_point_format():
    sign = input("ENTER THE SIGN ('+' , '-') : ")
    allBits = input("ENTER THE NUMBER OF ALL BITS : ")
    biasBits = input("ENTER THE NUMBER OF BIAS BITS : ")
    biNumber = input("ENTER THE BINARY NUMBER (IF THERE IS NO INPUT PLEASE EHTER '-') : ")

    if biNumber == '-':
        deciNumber = input("ENTER THE DECIMAL NUMBER : ")
        biNumber = deciToFractionProcess(deciNumber)
    
    # set sign
    if sign[0] == '+':
        sign = "0"
    elif sign[0] == '-':
        sign = "1"
    
    # normalize 
    biNumber = float(biNumber)
    jumpFlag = int(biNumber) > 1
    E = 0
    if int(biNumber) != 1:
        if jumpFlag == True:
            while jumpFlag:
                biNumber = biNumber / 10
                jumpFlag = int(biNumber) > 1
                E += 1

        elif jumpFlag == False:
            while not jumpFlag:
                biNumber = biNumber * 10
                jumpFlag = int(biNumber) > 0
                E -= 1
    biNumber = str(biNumber)
    fraction = biNumber[2:]

    # bias exponant
    bias = pow(2, int(biasBits)-1) - 1
    BE = E + bias
    
    # present and print it
    fractionBits = int(allBits) - int(biasBits) - 1
    if len(fraction) < fractionBits:
        addBits = fractionBits - len(fraction)
        fraction = fraction + ("0" * addBits)
    BEBi = get_unsigned_in_nbits(str(BE), biasBits)
    print(sign + "|" + BEBi + "|" + fraction[:fractionBits]) 

#### MAIN ####
if __name__ == "__main__" :
    # ### the start of printing results
    program()
    # ### the end of printing results
