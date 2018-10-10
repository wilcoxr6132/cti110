# Areas of Rectangles
# 10/5/2018
# CTI-110 P3T1_AreasOfRectangles  
# RaymondWilcox

# Get the lenght and width of rectangle 1
lenght1 = int(input("what is the lenght of rectangle 1? "))
width1 = int(input('what is the width of rectangle 1? '))

# Get the lenght and width of rectangle 2
lenght2 = int(input('what is the lenght of rectangle 2? '))
width2 = int(input('what is the width of rectangle 2? '))

# Calculate the area of the rectangles
area1 = lenght1 * width1
area2 = lenght2 * width2

# Wich rectangle is bigger?
if area1 > area2:
    print('Rectangle 1 is bigger.')
elif area2 > area1:
    print('Rectangle 2 is bigger.')
else:
    print("They are the same size!")
          
