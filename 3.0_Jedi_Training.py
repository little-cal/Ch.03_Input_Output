# 3.0 Jedi Training (20pts)  Name:________________


# In all the short programs below, do a good job communicating with your end user!


# 1. Write a program that asks someone for their name and then prints a greeting that uses their name. (1pt)
def greeting():
    # get string input from user, their name
    name = input("What is your name?\n")
    print("Hello, nice to meet you", name + "!")
    # printing a greeting specific to user


# greeting()
# 2. Write a program where a user enters a base and height, and you print the area of a triangle. (1pt)
def triangle():
    # Get integer values for base & height of a triangle
    base = int(input("What is the base of the triangle?\n:"))
    height = int(input("What is the height of the triangle?\n:"))
    # formula for area of triangle
    area = .5*base*height
    print("The area is: ", area)
    # printing the area of a triangle


# triangle()
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference. (1pt)
def circumference():
    # getting the integer input from user, the radius of a circle
    radius = int(input("What is the radius of the circle?\n:"))
    # formula for circumference and rounding it to 3 digits after the decimal
    circum = 2*3.14*radius
    circum = round(circum, 3)
    print("The circumference is:", circum)
    # printing the circumference of the circle, based on the given radius


# circumference()
# 4. Ask a user for an integer and then print the square root. (1pt)
def sqr_root():
    # asking the user for a number they would like the square root of
    num = int(input("What number would you like to find the square root of?\n:"))
    # formula for sqr root and rounding it to 3 decimal places
    sqrt = num**.5
    sqrt = round(sqrt, 3)
    print("The square root of", num, "is:", sqrt)
    # printing the square root of the number given


# sqr_root()
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next. (1pt)
def force():
    # asking for a float value of mass and acceleration
    m = float(input("What is the mass?\n:"))
    a = float(input("What is the acceleration?\n:"))
    # formula for force and printing the result
    f = m*a
    print("The Force is:", f)
    # printing the "get it" in itallic
    print("\x1B[3m" + 'Get it?' + "\x1B[0m")


# force()
'''
6. TEMPERATURE PROGRAM (5pts)
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test your program with the following data:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ??? Please tell me what this output is!
-40 in Fahrenheit is -40 in Celsius
'''


def temp_conv():
    # asking the user for the temperature they would like to convert
    temp1 = int(input("What is the temperature in Fahrenheit you would like to convert?\n: "))
    # formula for F -> C and rounding it one decimal place
    temp2 = (temp1-32)*(5/9)
    temp2 = round(temp2, 1)
    # printing what the first temp is in celsius
    print(temp1, "in Celsius is:", temp2)


# temp_conv()

'''
7. TRAPEZOID PROGRAM (5pts)
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print
the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''


def trap_area():
    # asking for user input of all the necessary info to get area of trapezoid
    b1 = float(input("What is one base of the trapezoid?\n:"))
    b2 = float(input("What is the second base of the trapezoid?\n:"))
    h = float(input("What is the height of the trapezoid?\n:"))
    # formula for trapezoid area
    a = ((b1+b2)/2)*h
    # printing the area
    print("The area of the trapezoid is:", a)


# trap_area()
'''
8. GRADING PROGRAM (5pts)
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''


def grade_calc():
    # getting user input, grades and exam weight
    sg = float(input("What was your semester grade?\n:"))
    fe = float(input("What was your final exam grade\n:"))
    ew = float(input("How much is the final exam worth?\n:"))
    '''
    Formula for this:
    - multiply exam weight by final exam grade
    - 100 - exam weight gets the weight of the semester grade
    - multiply that weight by the semester grade
    - divide by 100
    - add it together, gets you the overall grade for the class.
    '''
    fg = ((ew*fe) + (100-ew)*sg)/100
    print("Your overall grade for the class is:", fg)


# grade_calc()
