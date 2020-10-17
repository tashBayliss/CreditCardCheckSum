# credit card check sum

cardNumber = int(input("Enter a 16 digit number: "))

if (len(str(cardNumber)) != 16):
    print("Invalid card length")

else:
    #step1: Put in array    
    array = [int(i) for i in str(cardNumber)]

    #step2: Reverse the number
    array.reverse()

    #step3: A = sum of odd places
    A = 0

    for i in range (0, 16, 2):
        A = A + array[i]

    #step4: calculate B (times, add double digits, add together)
    B = 0
    result = 0

    for i in range (1, 16, 2):
        temp = array[i]*2

        if (len(str(temp)) == 2):
            number = sum((int(digit) for digit in str(temp)))
            B = B + number

        else:
            B = B + temp

    # step 4: If A+B is divisable by 10 then valid
    if ((A+B)%10 == 0):
        print("Valid")

    else:
        print("Invalid")