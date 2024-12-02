##### Program1:##########
## The expected output of the program###

#Sample example 1:
data=[10,501,22,37,100,999,87,351]  # Input
result = filter(lambda x : x > 4, data)
print(list(result)) ###### output is :[10,501,22,37,100,999,87,351]

#Sample example 2:
#In the above program it allows only the number which is greater than 4.
#For example the input is [1,2,3,10,501,22,37,100,999,87,351] in this case
#it filters the number below 4 value
data=[1,2,3,10,501,22,37,100,999,87,351]
result = filter(lambda x : x > 4, data)
print(list(result)) # output is :[10,501,22,37,100,999,87,351]

                        ##### Program2:##########
###Checking the integer or string found in the list##

#Sample list containing mixed data types
Data_list = [10, 30, 40, "Ant", 20, "animal", 2.3, 4.5, "bat"]

# Lambda function to check if an element is an integer or a string
check_type = lambda n: 'integer' if isinstance(n, int) else 'string' if isinstance(n, str) \
    else 'Not a string or Integer'

# Applying the lambda function to each element in the list
Output = list(map(check_type,Data_list))
print(Output)


#### Program3:##########
# Creating fibonacci series using lambda function from 1 to 50####
# Initializing the function using 'def'
def fibonacci(count):
    fib_list = [0, 1]
    # It uses the 'map()' function along with a lambda function and an initial list [0, 1]
    # to generate the Fibonacci series

    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
            range(2, count)))

    return fib_list[:count]


print("Fibonacci series upto 10:")
# Fibonacci limit is 50
print(fibonacci(10))
 ##############Program4:#############
####Validating email address using regular expression########

import re
#Initializing the function using 'def'
def Verify_email(email):
    pattern_for_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern_for_email, email))

# Example usage
print(Verify_email("example@example.com"))  # True
print(Verify_email("invalid-email.com"))    # False

########Validating Bangladeshi mobile number using regular expression##

##Initializing the function using 'def'
def verify_bangladesh_mobile(number):
    mobile_pattern = r'^01[3-9]\d{8}$'  # Starting with 01, followed by a digit between 3-9 and 8 other digits
    return bool(re.match(mobile_pattern, number))

# Example usage
print(verify_bangladesh_mobile("01712345678"))  # True
print(verify_bangladesh_mobile("0131234567"))   # False (because 13 is not valid)

#########Validating USA telephone number using regular expression##
# #Initializing the function using 'def'
def verify_usa_telephone(number):
    usa_telephone_pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(usa_telephone_pattern, number))

# Example usage
print(verify_usa_telephone("(123) 456-7890"))  # True
print(verify_usa_telephone("123-456-7890"))    # True
print(verify_usa_telephone("123 456 7890"))    # True
print(verify_usa_telephone("1234567890"))      # False


#########Validating Password using regular expression##

#Initializing the function using 'def'
def verify_password(password):
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{16}$'
    return bool(re.match(password_pattern, password))

# Example usage
print(verify_password("Password123!@#$"))
print(verify_password("short123"))
print(verify_password("password123!@#$"))