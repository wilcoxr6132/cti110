# CTI-110 
# P3HW1 - Roman Numerals
# Raymond Wilcox 
# 10/07/2018

# Converting numaric numbers to Roman numerals.

#Define the Main function.
def main():
    
# Have user enter a number
    userNumber = int(input('Please and enter a number '))

# Conversion from Numaric to Roman Numeral.
    if userNumber == 1:
        print("1 = I")
    elif userNumber == 2:
        print("2 = II")
    elif userNumber == 3:
        print("3 = III")
    elif userNumber == 4:
        print("4 = V")
    elif userNumber == 5:
        print("5 = VI")
    elif userNumber == 6:
        print("6 = VII")
    elif userNumber == 7:
        print("7 = VII")
    elif userNumber == 8:
        print("8 = VIII")
    elif userNumber == 9:
        print("9 = IX")
    elif userNumber == 10:
        print("10 = X")
    else:
        print("ERROR: Please enter a number between 1-10")
        
# Call the main function.
main()











