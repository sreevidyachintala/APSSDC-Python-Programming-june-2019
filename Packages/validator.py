import re
def phoneNumberValidator(number):
    pat="^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$"
    if re.match(pat,str(number)):
        return True
    else:
        return False
    return


import re
def emailValidator(email):
    pat='[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z0-9]{2,4}$'
    if re.match(pat,(email)):
        return True
    else:
        return False
    return
#emailValidator('vidyachintala22@gmail.com')
