print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import re

passworld=input("nhap cac mat khau , cach nhau bang giau phay:").split(',')
valid_passwords =[]

for p in passworld:
    p = p.strip()

    if len(p)<6 or len(p)>12:
        continue
    elif not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif  re.search("\s",p):
        continue
    valid_passwords.append(p)
print("mat khau hon le",",".join(valid_passwords))