import random as r
import string
def gen_pass(pass_length):
    elements = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(pass_length):
        password += r.choice(elements)

    return password

def suma(a,b):
    return a+b