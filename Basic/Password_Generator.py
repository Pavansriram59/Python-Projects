
# * Random password generator for your accounts

from random import *
from string import *

# ! Maximum length of random password
MAX_LEN=12

UNUSED_CHARACTERS=['"',"'",'(',')','.',',','<','>','[',']','{','}','^','~','`',':',';','+','=','-','|','*']
CHARACTERS=[x for x in list(printable) if x not in list(whitespace)]
CHARACTERS=[x for x in CHARACTERS if x not in UNUSED_CHARACTERS]
print(CHARACTERS)


def generate_password(MAX_LEN,CHARACTERS):
    rand_digit=choice(list(digits))
    rand_lower=choice(list(ascii_lowercase))
    rand_upper=choice(list(ascii_uppercase))
    rand_symbol=choice(list(punctuation))

    temp_pass=rand_digit+rand_lower+rand_upper+rand_symbol

    for x in range(MAX_LEN - 4): 
        temp_pass = temp_pass + choice(CHARACTERS) 
    
        
        temp_pass_list = list(temp_pass)
        shuffle(temp_pass_list)     
    password = "" 
    for x in temp_pass_list: 
        password = password + x 
             
    print(password) 

generate_password(MAX_LEN,CHARACTERS)

