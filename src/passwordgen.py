import random 
import array, re

def givepassword(test):
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                                            'z'] 
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                                            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                                            'Z'] 
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
                    '*', '(', ')'] 

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 

    rand_digit = random.choice(DIGITS) 
    rand_upper = random.choice(UPCASE_CHARACTERS) 
    rand_lower = random.choice(LOCASE_CHARACTERS) 
    rand_symbol = random.choice(SYMBOLS) 
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4): 
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass=list(temp_pass)
    random.shuffle(temp_pass)
    temp_pass=''.join(temp_pass)
    return temp_pass
def teststrength(word):
    password = word
    flag = 0
    warning='Weak Password\n'
    if (len(password)<8): 
        warning=warning+'Password Too Short'+'\n'
    if not re.search("[a-z]", password): 
        warning=warning+'No Small Letters Found'+'\n'
    if not re.search("[A-Z]", password): 
        warning=warning+'No Capital Letters Found'+'\n'
    if not re.search("[0-9]", password): 
        warning=warning+'No Numbers Found'+'\n'
    if not re.search("[_@$]", password): 
        warning=warning+'No Symbols Found'+'\n'
    if(warning==''):
        warning='It is a Good Password'
    return warning




