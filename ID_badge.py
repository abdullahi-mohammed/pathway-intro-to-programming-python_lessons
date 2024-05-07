# Author Abdullahi Mohammed
# Date   13th, jan. 2024.
# Purpose Learning how to use strings

first_name = input("input your First Name ")
last_name = input("input your Last name ")
email_address = input("input your Email Address ")
phone_number = input("input your Phone Number ")
job_title = input("input your Job Title ")
id_number = input("input your ID Number ")
hair_color = input("input hair color ")
eyes_color = input("input eyes color ")
month = input("input month ")
training_option = input("input training option(YES/NO) ")


print("The ID Card is:")
print("----------------------------------------")
print(last_name.upper() + ', ' + first_name.lower())
print(job_title.title())
print("ID: "+ id_number)
print('')
print(email_address.lower())
print(phone_number)
print('')
print( f"Hair:  {hair_color:10} Eyes:  {eyes_color}" )
print( f"Month:  {month:9} Training:  {training_option}" )
print("----------------------------------------")