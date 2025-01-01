import re

def password_strenght_checker (password):
    strength = 0

    if len (password)>=8:
        strength +=1
    if len (password)>=12:
        strength +=1
    if len (password)>=16:
        strength +=1
    
    if re.search(r'[a-z]', password):
        strength +=1
    if re.search(r'[A-Z]', password):
        strength +=1
    if re.search(r'[0-9]', password):
        strength +=1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength +=1
    

    if strength <3:
        return "weak"
    elif strength <5:
        return "medium"
    else :
        return "strong"
    

password = input ("inter your password to analize its strong")
strength = password_strenght_checker (password)
print (f"password strength : {strength }")


#by CY3ER
