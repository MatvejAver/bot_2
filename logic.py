from random import choice,randint
from requests import get

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = get(url)
        data = res.json()
        return data['url']

def len_password(password):
    len = False
    for i in range(1,1000):
        if password == str(i):
            len = True
            break
    
    return len

def password_gen(len):
    while True:
        accuracy = [False,False,False,False]
        password = ''
        symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890/*-+~`!@#$%^&*)(}{][;:""''|<,>.?/'
        for i in range(len):
            password += choice(symbols)

        for symb in password:
            for i in range(26,52):
                if symb == symbols[i]:
                    accuracy[0] = True
                    break
            
            for i in range(25):
                if symb == symbols[i]:
                    accuracy[1] = True
                    break

            for i in range(53,62):
                if symb == symbols[i]:
                    accuracy[2] = True
                    break

            for i in range(63,93):
                if symb == symbols[i]:
                    accuracy[3] = True
                    break

        if accuracy[0] == True and accuracy[1] == True and accuracy[2] == True and accuracy[3] == True:
            break
            
    return password