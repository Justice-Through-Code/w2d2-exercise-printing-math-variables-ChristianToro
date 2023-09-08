
def convert_100_to_celsius():
    celsius_100 = (100 - 32) * (5/9)
    print(float(celsius_100))
convert_100_to_celsius()
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    #The result will be a rational number because of the product of the difference of 100 and 32 and the quotient of 5/9
    #The division of 5/9 will force all of the resulting outputs to be a float type

def convert_0_to_celsius():
    celsius_0 = (100 - 32) * (5/9)
    print(float(celsius_0))
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value

convert_0_to_celsius()

def convert_34_2_to_celsius():
    print(float((34.2 - 32) * (5/9)))
convert_34_2_to_celsius()
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    
#convert_34_2_to_celsius()


# Now, can you convert back?


def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    print(float((5 *(9/5)) + 32))

convert_5_to_fahrenheit()

def hotter_temp():
    temp1 = float((85.1 - 32) * (5/9))
    temp2 = 30.2
    if temp1 > temp2:
        print('85.1 degrees fahrenheit is hotter than 30.2 degrees celsius')
    else:
        print('30.2 degrees celsius is hotter than 85.1 degrees fahrenheit')
    
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively

hotter_temp()