name = 'Imtiaz Abedin'
try:
    # Write the suspicious block of code
    print(name[15])
except AssertionError:  # Catch a single exception
    # This block will be executed if exception A is caught
    print('AssertionError')
except (EnvironmentError, SyntaxError, NameError) as E:  # catch multiple exception
    # This block will be executed if any of the exception B, C or D is caught
    print(E)
except:
    print('Exception')
    # This block will be executed if any other exception other than A, B, C or D is caught
else:
    # If no exception is caught, this block will be executed
    pass
finally:
    # This block will be executed and it is a must!
    pass

# this line is not related to the try-except block
print('This will be printed.')
