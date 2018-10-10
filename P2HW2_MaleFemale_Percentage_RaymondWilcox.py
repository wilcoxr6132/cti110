# Male and Female Percantages
# 09/26/2018
# CTI-110 P2HW2-Male Female
# Raymond Wilcox




# Program to find percentages of males to females

# Number of males in the class
males = float(input('How many males are in the class: '))

# Number of females in the class
females = float(input('How many females are in the class: '))

# Total number of students
TotalStudents = males + females

# Percent of males in the class
PercentMales = (males / TotalStudents) 

# Percent of females in the class
PercentFemales = (females / TotalStudents) 

# Percentage results
print( 'There are' , TotalStudents , "TotalStudents in the class. " , format( PercentMales  , '.2%' ) , "of them are males" )

