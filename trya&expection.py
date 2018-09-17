try : 
    number = float(input("Enter any value you reqire to test the TRY and expection handling"))
    result = (100.00/number)
    print()
    print("Result is " ,result)


except :
    print()
    print("Invalid input given by the user as well ")

finally:
    print()
    print("Finally block a message")
    print()


print("This message will there if there in expection in the input line")
    
