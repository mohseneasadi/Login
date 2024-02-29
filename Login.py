# this is a code that get the name, password and email from user. Maybe users
# input whatever they want but that's not acceptable, the name must be alphabetic whitout numbers, 
# password must be combination of numbers and alphabet charachters (both upper-lowercase) 
# and email must be contain of '@'.

# -------------------------------------------------#
# Define variables
alpha_pass = ""
alphabet_lower = "abcdefghijklmnopqrstuvwxyz" 
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
email_check = "@"

print ('----------------------------------')
#this part asks users to input thier name, then check the name that be without numbers 

done = True
while done == True :

    try :   
        name = input('Please enter your name: ')
        name = name.strip()
        name_up = name.upper()

        for letters in name :
            if letters.isdecimal() :
                raise Exception ("That's not acceptable! Name must be a string type without numbers")

        print ('----------------------------------')
    
#this part asks users to choose thier password, then check the password that must be between (8-20) 
# and contain both numbers and alphabet charachters (upper & lowercase)
    
        password = input('please enter a password: ')
        password = password.strip()
        len_password = len(password)

        if not len_password in range(8, 21) :
            raise Exception (f"Your password has {len_password} characters, it must have between 8 - 20 charachters")

        pass_check = password.isnumeric()
        if  pass_check == True : 
            raise Exception ("Sorry!your password must be mix of numeric and alphabet")
    
        pass_check = password.isalpha()
        if  pass_check == True : 
            raise Exception ("Sorry!your password must have atleast one 'Number'!")
    
        for letters in password :
            if letters.isdecimal() :
                continue #logic error: I forgot putting this (continue) in the loop, so it just checked the first letter and break the loop.
            elif letters.isalpha() :
                alpha_pass = alpha_pass + letters 
    
        for i in alpha_pass : 
            if not i in alphabet_lower :
                continue #logic error: I forgot putting this (continue) in the loop, so it just checked the first letter and break the loop.
            elif i in alphabet_lower : 
                break
        else :
            raise Exception("Sorry! your password must have atleast one 'Lowercase'!")
        
        for i in alpha_pass :  
            if not i in alphabet_upper :
                continue #logic error: I forgot putting this (continue) in the loop, so it just checked the first letter and break the loop.
            elif i in alphabet_upper :
                break
        else :
            raise Exception("Sorry! your password must have atleast one 'Uppercase'!")
    
        print("\nGood job! it's a strong password")

        print('----------------------------------')

#this part asks users to choose thier emails and it must be contain of '@'.
    
        email = input('please enter your email: ')  
        email = email.strip()

        for items in email : 
            if email[0] == "@" :
                raise Exception ("Sorry! your email must be valid! You can't use @ at first of your email")
                break
            elif not items in email_check :
                continue
            elif items in email_check :
                done = False
                break
        else : 
            raise Exception("Sorry! your email must be valid! Don't forget write your complete email address with '@...' ")

        print('----------------------------------')

    except Exception as e : 
        print(e)

    else :
        print(f"That's great! Wellcome {name_up}!\nThis is your username: {email} \nThis is your password: {password}")
print('----------------------------------')