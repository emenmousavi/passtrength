import string

def passtrength(passwd):
    has_upper = False
    has_digit = False
    has_symbol = False
    
    symbol = string.punctuation
    
    if len(passwd) < 8:
        return "Weak password: Too short!"
    
    for char in passwd:
        if char.isdigit():                
            has_digit = True
        if char.isupper():
            has_upper = True
        if char in symbol:
            has_symbol = True
            
    if has_upper and has_digit and has_symbol:
        return "Password is strong enough"
    elif not has_upper:
        return "Weak password: Missing an uppercase"
    elif not has_digit:
        return "Weak password: Missing a digit"
    elif not has_symbol:
        return "Weak password: Missing a symbol"

password = input("Enter your password: ")
print(passtrength(password))
