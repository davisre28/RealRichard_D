##                                                          ##
## Calculator Application for SWEN4342.02 by Team SARN      ##
##                                                          ##
## Authors:                                                 ##
##                                                          ##
## Saif Ul Islam, Asad Raza, Richard Davis, Noman Mansuri   ##
##                                                          ##

import struct
import ctypes
import decimal
import math

#Implementation of Values class getters & setters
class Value:
    def _init_(value_type):
        value_type._value = 0
    def get_value(value_type):
        return value_type._value
    def set_value(value_type, v):
        value_type._value = v
    def del_value(value_type):
        del value_type._value
    value = property(get_value, set_value, del_value)
    

#Define and calculate Add
def Add(a,b):
    try:
        val1 = a
        val2 = b
        print()

        add = Value()
        add.value = (val1+val2)
        return add.value

    except ValueError:
                print("\nInvalid entry 1 line 39\n")
        

#Define and calculate Subtract
def Subtract(a,b):
    try:
        val1 = a
        val2 = b
        print()

        subtract = Value()
        subtract.value = (val1-val2)
        return subtract.value

    except ValueError:
        print("\nInvalid entry 2 line 54\n")
                    
        
#Define and calculate Multiply
def Multiply(a,b):
    try:
        val1 = a
        val2 = b
        print()
        
        multiply = Value()
        multiply.value = (val1*val2)
        return multiply.value

    except ValueError:
        print("\nInvalid entry 3 line 69\n")
        

#Define float operational choices
def FloatOperation():
    
    choices = ['1','2','3','4']
    choice = input("\nSelect from the following choices:\n\n1 for Add\n2 for Subtract\n3 for Multiply\n4 to convert or show output\n\n Your Choice: ")
    print()
    try:
        while choice in choices:
                        
            if(choice == '1'):
                result = Add(UserInputFloat1(),UserInputFloat2())
                return result
                break
                            
            if(choice == '2'):
                result = Subtract(UserInputFloat1(),UserInputFloat2())
                return result
                break
                            
            if(choice == '3'):
                result = Multiply(UserInputFloat1(),UserInputFloat2())
                return result
                break

            if(choice == '4'):
                result = UserInputFloat1()
                return result
                break

    except TypeError:
        print("***Invalid entry. Please try again.*** 4 line 102\n")


#Define Hex operational choices
def HexOperation():
    
    choices = ['1','2','3','4']
    choice = input("\nSelect from the following choices:\n\n1 for Add\n2 for Subtract\n3 for Multiply\n4 to convert or show output\n\n Your Choice: ")
    print()
    try:
        while choice in choices:
                        
            if(choice == '1'):
                result = Add(UserInputHex1(),UserInputHex2())
                return result
                break
                            
            if(choice == '2'):
                result = Subtract(UserInputHex1(),UserInputHex2())
                return result
                break
                            
            if(choice == '3'):
                result = Multiply(UserInputHex1(),UserInputHex2())
                return result
                break

            if(choice == '4'):
                result = UserInputHex1()
                return result
                break

    except TypeError:
        print("***Invalid entry. Please try again.*** 5 line 135\n")


#Define Binary operational choices
def BinOperation():
    
    choices = ['1','2','3','4']
    choice = input("\nSelect from the following choices:\n\n1 for Add\n2 for Subtract\n3 for Multiply\n4 to convert or show output\n\n Your Choice: ")
    print()
    try:
        while choice in choices:
                        
            if(choice == '1'):
                result = Add(UserInputBin1(),UserInputBin2())
                return result
                break
                            
            if(choice == '2'):
                result = Subtract(UserInputBin1(),UserInputBin2())
                return result
                break
                            
            if(choice == '3'):
                result = Multiply(UserInputBin1(),UserInputBin2())
                return result
                break

            if(choice == '4'):
                result = UserInputBin1()
                return result
                break

    except TypeError:
        print("***Invalid entry. Please try again.*** 6 line 168\n")


#Define Binary operational choices
def SignExponentMantissaOperation():
    
    choices = ['1','2','3','4']
    choice = input("\nSelect from the following choices:\n\n1 for Add\n2 for Subtract\n3 for Multiply\n4 to convert or show output\n\n Your Choice: ")
    print()
    try:
        while choice in choices:
                        
            if(choice == '1'):
                result = Add(UserInputSignExpMan1(),UserInputSignExpMan2())
                return result
                break
                            
            if(choice == '2'):
                result = Subtract(UserInputSignExpMan1(),UserInputSignExpMan2())
                return result
                break
                            
            if(choice == '3'):
                result = Multiply(UserInputSignExpMan1(),UserInputSignExpMan2())
                return result
                break

            if(choice == '4'):
                result = UserInputSignExpMan1()
                return result
                break

    except TypeError:
        print("***Invalid entry. Please try again.*** 7 line 201\n")


#Convert Hex to Decimal
def HexToDecimal(n):
    try:
        decimal = int(n, 16)
        return decimal
        
    except ValueError:
        print("\nInvalid entry 8 line 211\n")


#Convert Hex to Binary
def HexToBinary(n):
    try:
        decimal = HexToDecimal(n)
        binary = DecimalTo32bitBinary(decimal)
        return binary

    except TypeError:
        print("\nInvalid entry 9 line 222\n")


#Convert Binary to Hex
def BinaryToHex(n):
    try:
        return DecimalToHex(BinaryToDecimal(n))

    except TypeError:
        print("\nInvalid entry 10 line 231\n")
        

#Convert int to Hex
def DecimalToHex(n):
    val1 = int(n)
    try:
        #return hex(int(n))
        digits = "0123456789ABCDEF"
        x = (val1 % 16)
        rest = val1 // 16
        if (rest == 0):
            return digits[x]
        return DecimalToHex(rest) + digits[x]
        
    except TypeError:
        print("\nInvalid entry 11 line 247\n")

        
#Convert Binary to Decimal
def BinaryToDecimal(a):
        val1 = a
        try:
            decimal = int(val1,2)
            return decimal

        except ValueError:
            print("\nInvalid entry 12 line 258\n")


#Convert int to 32-bit Binary
def DecimalTo32bitBinary(n):
    try:
        return "{:032b}".format(int(n))

    except TypeError:
        print()


#Convert Binary to Float
def BinaryToFloat(binary):

    try:
        return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

    except TypeError:
        print()
    except struct.error:
        print("\nArgument out of range 13 line 279\n")


#Convert Decimal to Exponent (SignExpMan)  ###***NOTE*** May still need work.... current code is Exponent for testing
def DecimalToSignExpMan(d):
    try:
#        return (BinaryToFloat(DecimalTo32bitBinary(n)))
#        return math.frexp(n)
        try:
            def RemainderToBinary(f):
                Bin = str()
                while(f):
                    f *= 2
                    if (f >= 1):
                        integer = 1
                        f -= 1
                    else: integer = 0
                    Bin += str(integer)
                    return Bin
                
        except ValueError:
            print("\nInvalid entry 14 line 300\n")
        except TypeError:
            print("\nInvalid entry. This is not a number (NaN) 15 line 302\n")

        try:
            def DecToFloat(n):
                sign = 0
                if(n < 0):
                    sign = 1
                n = abs(n)
                integer = (bin(int(n))[2:])
                remain = (RemainderToBinary(n - int(n)))
                i = integer.index('1')
                exp = (bin((len(integer)-i-1)+127)[2:])
                man = (integer[i+1:]+remain)
                man = (man+('0'*(23-len(man))))
                return sign, exp, man

        except ValueError:
            print("\nInvalid entry 16 line 319\n")

        try:
            sign, exp, man = DecToFloat(d)
            x = (str(sign) + '|' + exp + '|' + man)
            return x
        
        except ValueError:
            print("\nInvalid entry 17 line 327\n")     
        

    except ValueError:
        print("\nInvalid entry 18 line 331\n")
    except TypeError:
        print("\nInvalid entry. This is not a number (NaN) 19 line 333\n")





#Convert SignExpMan to Decimal  ###****NOTE*** May need additional work for handling exceptions/incorrect input. Will also be used for SignExpMan1 & SignExpMan2
def SignExpManToDecimal(f):
    try:
        try:
            def toInt(n):
                negCount = -1
                man = 0
                for iteration in n:
                    man += (int(iteration)*pow(2,negCount))
                    negCount -= 1
                return (man + 1)
            
        except ValueError:
            print("\nInvalid entry 20 line 352\n")

        try:
            SEM = f
            sign = int(SEM[0])
            expOffset = int(SEM[2:10],2)
            sub127 = (expOffset -127)
            n = (SEM[11:])
            man = toInt(n)
            number = (pow(-1,sign)*man*pow(2,sub127))
            return number
        
        except ValueError:
            print("\nInvalid entry 21 line 365\n")
            
    except ValueError:
        print("\nInvalid entry 22 line 368\n")
        
        
#Convert SignExpMan to Hex
def SignExpManToHex(n):

    try:
        return DecimalToHex(SignExpManToDecimal(n))

    except ValueError:
        print("\nInvalid entry 23 line 378\n")
        
        
#Convert SignExpMan to Binary
def SignExpManToBinary(n):

    try:
        return DecimalTo32bitBinary(SignExpManToDecimal(n))

    except ValueError:
        print("\nInvalid entry 24 line 388\n")


#Define numeric value type choices
def ValType():
    input_choices = ['1','2','3','4',]
    input_choice = input("\nSelect the input value type:\n\n1 for Decimal value          (for example 345.26)\n"
                    + "2 for Binary                 (for example 01000111010...)\n3 for Hexadecimal            (for example 3F9E147B)\n4 for Sign Exponent Mantissa (for example 1|10000000|00100000000000000000000)\n\n Your Choice: ")
    print()
    
    #while input_choice in input_choices:
    loop = True
    while loop:

        #Input Decimal
        if(input_choice == '1'):
            try:
                output_choices = ['1','2','3','4',]
                output_choice = input("\nSelect the output value type:\n\n1 for Decimal value          (for example 345.26)\n"
                                + "2 for Binary                 (for example 01000111010...)\n3 for Hexadecimal            (for example 3F9E147B)\n4 for Sign Exponent Mantissa (for example 1|10000000|00100000000000000000000)\n\n Your Choice: ")
                print()
                
                #while choice in choices:
                loop2 = True
                while loop2:

                    #Output Decimal
                    if(output_choice == '1'):
                        try:
                            result = FloatOperation()
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 25 line 423\n")
                        break

                    #Output Binary
                    elif(output_choice == '2'):
                        try:
                            result = DecimalTo32bitBinary(FloatOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 26 line 435\n")
                        break

                    #Output Hex
                    elif(output_choice == '3'):
                        try:
                            result = DecimalToHex(FloatOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 27 line 447\n")
                        break
                    
                    #Output SignExpMan
                    elif(output_choice == '4'):
                        try:
                            additional_output_choices = ['1','2']
                            additional_output_choice = input("\nSelect from the following additional output choices or enter\nany other value to skip this option and "
                                                        + "continue to the next selection:\n\n1 for Binary      (for example 01000111010...)"
                                                        + "\n2 for Hexadecimal (for example 3F9E147B)\n\n Your Choice: ")
                            print()
                            
                            #while additional_output_choice in additional_output_choices:
                            loop3 = True
                            while loop3:
                                
                                #Binary
                                if(additional_output_choice == '1'):
                                    try:
                                        x = FloatOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalTo32bitBinary(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Binary value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 28 line 476\n")
                                    break

                                #Hex
                                elif(additional_output_choice == '2'):
                                    try:
                                        x = FloatOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalToHex(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Hexadecimal value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 29 line 492\n")
                                    break

                                #Skip to result
                                while additional_output_choice not in additional_output_choices:
                                    loop3 = False
                                    print("\nNo valid additional choice was entered. Program will skip the additional output option and continue with the next selection below:\n")
                                    try:
                                        result = DecimalToSignExpMan(FloatOperation())
                                        if result is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result, "\n")
                                        #Comment in if needed for GUI -># return result
                                    except TypeError:
                                        print("\n***Invalid entry. Please try again.*** 30 line 506\n")
                                    break
                                
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 31 line 510\n")
                        break


                    while output_choice not in output_choices:
                        loop2 = False
                        print("***Invalid entry. Please try again.*** 32 line 516\n")
                        break                    

            except TypeError:
                print("***Invalid entry. Please try again.*** 33 line 520\n")

            break

        #Input Binary
        elif(input_choice == '2'):
            try:
                output_choices = ['1','2','3','4',]
                output_choice = input("\nSelect the output value type:\n\n1 for Decimal value          (for example 345.26)\n"
                                + "2 for Binary                 (for example 01000111010...)\n3 for Hexadecimal            (for example 3F9E147B)\n4 for Sign Exponent Mantissa (for example 1|10000000|00100000000000000000000)\n\n Your Choice: ")
                print()
                
                #while choice in choices:
                loop2 = True
                while loop2:

                    #Output Decimal
                    if(output_choice == '1'):
                        try:
                            result = BinOperation()
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 34 line 545\n")
                        break

                    #Output Binary
                    elif(output_choice == '2'):
                        try:
                            result = DecimalTo32bitBinary(BinOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 35 line 557\n")
                        break

                    #Output Hex
                    elif(output_choice == '3'):
                        try:
                            result = DecimalToHex(BinOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 36 line 569\n")
                        break

                    #Output SignExpMan
                    elif(output_choice == '4'):
                        try:
                            additional_output_choices = ['1','2']
                            additional_output_choice = input("\nSelect from the following additional output choices or enter\nany other value to skip this option and "
                                                        + "continue to the next selection:\n\n1 for Binary      (for example 01000111010...)"
                                                        + "\n2 for Hexadecimal (for example 3F9E147B)\n\n Your Choice: ")
                            print()
                            
                            #while choice in choices:
                            loop3 = True
                            while loop3:
                                
                                #Binary
                                if(additional_output_choice == '1'):
                                    try:
                                        x = BinOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalTo32bitBinary(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Binary value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 37 line 598\n")
                                    break

                                #Hex
                                elif(additional_output_choice == '2'):
                                    try:
                                        x = BinOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalToHex(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Hexadecimal value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 38 line 614\n")
                                    break

                                #Skip to result
                                while additional_output_choice not in additional_output_choices:
                                    loop3 = False
                                    print("\nNo valid additional choice was entered. Program will skip the additional output option and continue with the next selection below:\n")
                                    try:
                                        result = DecimalToSignExpMan(BinOperation())
                                        if result is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result, "\n")
                                        #Comment in if needed for GUI -># return result
                                    except TypeError:
                                        print("***Invalid entry. Please try again.*** 39 line 628\n")
                                    break
                                
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 40 line 632\n")
                        break

                    while output_choice not in output_choices:
                        loop2 = False
                        print("***Invalid entry. Please try again.*** 41 line 637\n")
                        break

            except TypeError:
                print("***Invalid entry. Please try again.*** 42 line 641\n")

            break

        #Input Hex
        elif(input_choice == '3'):
            try:
                output_choices = ['1','2','3','4',]
                output_choice = input("\nSelect the output value type:\n\n1 for Decimal value          (for example 345.26)\n"
                                + "2 for Binary                 (for example 01000111010...)\n3 for Hexadecimal            (for example 3F9E147B)\n4 for Sign Exponent Mantissa (for example 1|10000000|00100000000000000000000)\n\n Your Choice: ")
                print()
                
                #while choice in choices:
                loop2 = True
                while loop2:

                    #Output Decimal
                    if(output_choice == '1'):
                        try:
                            result = HexOperation()
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 43 line 666\n")
                        break

                    #Output Binary
                    elif(output_choice == '2'):
                        try:
                            result = DecimalTo32bitBinary(HexOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 44 line 678\n")
                        break

                    #Output Hex
                    elif(output_choice == '3'):
                        try:
                            result = DecimalToHex(HexOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 45 line 690\n")
                        break

                    #Output SignExpMan
                    elif(output_choice == '4'):
                        try:
                            additional_output_choices = ['1','2']
                            additional_output_choice = input("\nSelect from the following additional output choices or enter\nany other value to skip this option and "
                                                        + "continue to the next selection:\n\n1 for Binary      (for example 01000111010...)"
                                                        + "\n2 for Hexadecimal (for example 3F9E147B)\n\n Your Choice: ")
                            print()
                            
                            #while choice in choices:
                            loop3 = True
                            while loop3:
                                
                                #Binary
                                if(additional_output_choice == '1'):
                                    try:
                                        x = HexOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalTo32bitBinary(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Binary value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 46 line 719\n")
                                    break

                                #Hex
                                elif(additional_output_choice == '2'):
                                    try:
                                        x = HexOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalToHex(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Hexadecimal value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 47 line 735\n")
                                    break

                                #Skip to result
                                while additional_output_choice not in additional_output_choices:
                                    loop3 = False
                                    print("\nNo valid additional choice was entered. Program will skip the additional output option and continue with the next selection below:\n")
                                    try:
                                        result = DecimalToSignExpMan(HexOperation())
                                        if result is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result, "\n")
                                        #Comment in if needed for GUI -># return result
                                    except TypeError:
                                        print("***Invalid entry. Please try again.*** 48 line 749\n")
                                    break
                                
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 49 line 753\n")
                        break

                    while output_choice not in output_choices:
                        loop2 = False
                        print("***Invalid entry. Please try again.*** 50 758\n")
                        break

            except TypeError:
                print("***Invalid entry. Please try again.*** 51 line 762\n")

            break

        #Input SignExpMan
        elif(input_choice == '4'):
            try:
                output_choices = ['1','2','3','4',]
                output_choice = input("\nSelect the output value type:\n\n1 for Decimal value          (for example 345.26)\n"
                                + "2 for Binary                 (for example 01000111010...)\n3 for Hexadecimal            (for example 3F9E147B)\n4 for Sign Exponent Mantissa (for example 1|10000000|00100000000000000000000)\n\n Your Choice: ")
                print()
                
                #while output_choice in output_choices:
                loop2 = True
                while loop2:

                    #Output Decimal
                    if(output_choice == '1'):
                        try:
                            result = SignExponentMantissaOperation()
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 52 line 787\n")
                        break

                    #Output Binary
                    elif(output_choice == '2'):
                        try:
                            result = DecimalTo32bitBinary(SignExponentMantissaOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 53 line 799\n")
                        break

                    #Output Hex
                    elif(output_choice == '3'):
                        try:
                            result = DecimalToHex(SignExponentMantissaOperation())
                            if result is None:
                                raise TypeError
                            else: print("The result is:\n\n", result, "\n")
                            #Comment in if needed for GUI -># return result
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 54 line 811\n")
                        break

                    #Output SignExpMan
                    elif(output_choice == '4'):
                        try:
                            additional_output_choices = ['1','2']
                            additional_output_choice = input("\nSelect from the following additional output choices or enter\nany other value to skip this option and "
                                                        + "continue to the next selection:\n\n1 for Binary      (for example 01000111010...)"
                                                        + "\n2 for Hexadecimal (for example 3F9E147B)\n\n Your Choice: ")
                            print()
                            
                            #while choice in choices:
                            loop3 = True
                            while loop3:
                                
                                #Binary
                                if(additional_output_choice == '1'):
                                    try:
                                        x = SignExponentMantissaOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalTo32bitBinary(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Binary value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 55 line 840\n")
                                    break

                                #Hex
                                elif(additional_output_choice == '2'):
                                    try:
                                        x = SignExponentMantissaOperation()
                                        result1 = DecimalToSignExpMan(x)
                                        result2 = DecimalToHex(x)
                                        if result1 is None:
                                            raise TypeError
                                        elif result2 is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result1, "\n\n The Hexadecimal value is:\n\n", result2, "\n")
                                        #Comment in if needed for GUI -># return result1 and return result2
                                    except TypeError:
                                        print("\n***One of your entries had a TypeError. Please try again.*** 56 line 856\n")
                                    break

                                #Skip to result
                                while additional_output_choice not in additional_output_choices:
                                    loop3 = False
                                    print("\nNo valid additional choice was entered. Program will skip the additional output option and continue with the next selection below:\n")
                                    try:
                                        result = DecimalToSignExpMan(SignExponentMantissaOperation())
                                        if result is None:
                                            raise TypeError
                                        else: print("\nThe Sign Exponent Mantissa result is:\n\n(Sign | Exponent | Mantissa):\n\n", result, "\n")
                                        #Comment in if needed for GUI -># return result
                                    except TypeError:
                                        print("***Invalid entry. Please try again.*** 57 line 870\n")
                                    break
                                
                        except TypeError:
                            print("***Invalid entry. Please try again.*** 58 line 874\n")
                        break

                    while output_choice not in output_choices:
                        loop2 = False
                        print("***Invalid entry. Please try again.*** 59 line 879\n")
                        break

            except TypeError:
                print("***Invalid entry. Please try again.*** 60 line 883\n")
  #just added              
        while input_choice not in input_choices:
            loop = False
            print("***Invalid entry. Please try again.*** 61 line 887\n")
            break   
            #break


#Define user input Float- To use: UserInputFloat1(),UserInputFloat2()
def UserInputFloat1():
    loop = True
    while loop:
        try:
            x = input("Enter first floating point or decimal value: ")
            return float(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 62 line 903\n")


def UserInputFloat2():
    loop = True
    while loop:
        try:
            x = input("Enter second floating point or decimal value: ")
            return float(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 63 line 916\n")


#UserInputHex1 Fix
def hex1(n):
    try:
        decimal = int(n, 16)
        return decimal
                        
    except ValueError:
        print("\nInvalid entry, please try again 64 line 926\n")
        x = UserInputHex1()
        return x


#UserInputHex2 Fix
def hex2(n):
    try:
        decimal = int(n, 16)
        return decimal
                        
    except ValueError:
        print("\nInvalid entry, please try again 65 line 938\n")
        x = UserInputHex2()
        return x


#Define user input Hex- To use: UserInputHex1(),UserInputHex2()
def UserInputHex1():
    loop = True
    while loop:
        try:
            x = input("Enter first hexadecimal value: ")
            return hex1(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 66 line 954\n")


def UserInputHex2():
    loop = True
    while loop:
        try:
            x = input("Enter second hexadecimal value: ")
            return hex2(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 67 line 967\n")

            
#UserInputBin1 Fix
def bin1(n):
    val1 = n
    try:
        decimal = int(val1,2)
        return decimal
                        
    except ValueError:
        print("\nInvalid entry, please try again 68 line 978\n")
        x = UserInputBin1()
        return x

#UserInputBin2 Fix
def bin2(n):
    val1 = n
    try:
        decimal = int(val1,2)
        return decimal
                        
    except ValueError:
        print("\nInvalid entry, please try again 69 line 990\n")
        x = UserInputBin2()
        return x
            

#Define user input Binary- To use: UserInputBin1(),UserInputBin2()
def UserInputBin1():
        
    loop = True
    while loop:
        try:
            x = input("Enter first binary value: ")
            return bin1(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 70 line 1007\n")


def UserInputBin2():
    loop = True
    while loop:
        try:
            x = input("Enter second binary value: ")
            return bin2(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 71 line 1020\n")


#UserInputSignExpMan1 Fix  ###***NOTE*** Fixes will need the following code copied from above def: SignExpManToDecimal()
def SignExpMan1(f):
    try:
        try:
            def toInt(n):
                negCount = -1
                man = 0
                for iteration in n:
                    man += (int(iteration)*pow(2,negCount))
                    negCount -= 1
                return (man + 1)
            
        except ValueError:
            print("\nInvalid entry 72 line 1036\n")

        try:
            SEM = f
            sign = int(SEM[0])
            expOffset = int(SEM[2:10],2)
            sub127 = (expOffset -127)
            n = (SEM[11:])
            man = toInt(n)
            number = (pow(-1,sign)*man*pow(2,sub127))
            return float(number)

        except ValueError:
            print("\nInvalid entry\n")
            
    except ValueError:
        print("\nInvalid entry, please try again 73 line 1052\n")
        x = UserInputSignExpMan1()
        return x


#UserInputSignExpMan2 Fix  ###***NOTE*** Fixes will need the following code copied from above def: SignExpManToDecimal()
def SignExpMan2(f):
    try:
        try:
            def toInt(n):
                negCount = -1
                man = 0
                for iteration in n:
                    man += (int(iteration)*pow(2,negCount))
                    negCount -= 1
                return (man + 1)
            
        except ValueError:
            print("\nInvalid entry 74 line 1070\n")

        try:
            SEM = f
            sign = int(SEM[0])
            expOffset = int(SEM[2:10],2)
            sub127 = (expOffset -127)
            n = (SEM[11:])
            man = toInt(n)
            number = (pow(-1,sign)*man*pow(2,sub127))
            return float(number)

        except ValueError:
            print("\nInvalid entry 75 line 1083\n")
        
    except ValueError:
        print("\nInvalid entry, please try again 76 line 1086\n")
        x = UserInputSignExpMan2()
        return x


#Define user input SignExpMan- To use: UserInputSignExpMan1(),UserInputSignExpMan2()
def UserInputSignExpMan1():
    loop = True
    while loop:
        try:
            x = input("Enter first Sign | Exponent | Mantissa value: ")
            return SignExpMan1(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 77 line 1102\n")


def UserInputSignExpMan2():
    loop = True
    while loop:
        try:
            x = input("Enter second Sign | Exponent | Mantissa value: ")
            return SignExpMan2(x)
            loop = False
            break

        except ValueError:
            print("\nInvalid entry 78 line 1115\n")



#Main Program:
def Main():
    #User input for answer
    answer = ['yes','YES','Yes','y','Y']
    repeat = 'yes'
        
    #Loop for answer
    while repeat in answer:
        ValType()
        
        repeat = input("Would you like to continue?\n\n")
            
    else: print("\nThe program will now exit.")

#Calling Main()
Main()
