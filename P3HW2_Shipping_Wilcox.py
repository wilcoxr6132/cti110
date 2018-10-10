# CTI-110 
# P3HW2 - Shipping Charges 
# Raymond Wilcox 
# 10/07/2018

# Difine the main function
def main():

# ask user to enter shipping weight.
    packageWeight = int(input("please enter the weight of your package "))

# Converting weight into price.
    if packageWeight < 2:
        print('your charge is $1.50 ')

    elif packageWeight > 2 and packageWeight <= 6:
        print('your charge is $3.00 ')
    elif packageWeight > 6 and packageWeight <= 10:
        print('your charge is $4.00 ')
    elif packageWeight > 10:
        print('your charge is $4.75 ')
        
# Call the main function.
main()



