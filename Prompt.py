#import the getpass method from the  getpass python package
#The getpass  method ensures password is not visible when the user enters it.
from getpass import getpass  
# from getpass import*

#prompt user to enter his/her details
fn=input('Input your first name ')  
sn=input('Input your second name ')
em=input('Enter your email address ')

# prompt user to enter his/her password using the getpass method

pssd=getpass('Input your password')

# print the user's information
print("\nDetails:")
print("First name:{}".format(fn))
print("second name:{}".format(sn))
print("Email address:{}".format(em))


# Write a program that can prompt the user to enter first name,second name and email.and on inputting the password it prints the first name,second name and email