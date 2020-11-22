def password_checker():
    password = input("Enter a password. Your password should contain a mixture of letters, numbers and special characters, and at least 8 characters long: ")
    u, l, sc, n = 0,0,0,0
    special_characters = ['!', '@', '£', '$', '%', '^', '&', '*', '#', '~', '/', '?']
    password_strength = True
    #u = upper case, l= lower case, sc = special character, n = number
    if (len(password) < 8):
        password = input("Password not long enough, choose a password at least 8 characters long: ")
    while (u < 1 and l < 1 and sc < 1 and n < 1 and (u+l+sc+n != len(password))):
        for i in range(len(password)):
            if password[i].isupper():
                u += 1
            elif password[i].islower():
                l += 1
            elif password[i] in special_characters:
            #((password[i] == '@') or (password[i] == "!") or (password[i] == "$") or (password[i] == "£") or (password[i] == "#") or (password[i] == "%") or 
            (password[i] == "&") or (password[i] == "*") or (password[i] == "?") or (password[i] == "/") or (password[i] == "~")):
                sc += 1
            elif password[i].isdigit():
                n += 1
    if (u >= 1 and l >= 1 and sc >= 1 and n >= 1 and (u+l+sc+n == len(password))):
        password_strength = True
        print("Your password is strong enough.")
    else:
        password_strength = False
        print("Your password is not strong enough.")
    return password_strength

password_checker()
