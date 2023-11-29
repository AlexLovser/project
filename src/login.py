profs = {
    'alaa':'sdazd',
    'alex':'dqdqs',
    'dib':'sqds',
}
s = True
while s == True:
    quis = input('Do u Have profile here (y/n) or stop : ')
    if quis == 'y':
        print('*****LOGIN SCREEN*****')
        nickNama = input("Entrez ton NickName : ")
        password = input("Entrez ton Password : ")
        if nickNama in profs:
            if profs[nickNama] == password :
                print('done login')
            else:
                print("password is error")
        else :
            print("user not exist")
    elif quis == 'n' :
        print('*****SING UP SCREEN*****')
        nickNama = input("Entrez ton NickName : ")
        password = input("Entrez ton Password : ")
        if nickNama not in profs:
            profs [nickNama] = password
            print("done sign up")
        else :
            print("Le prof existe déjà")
    elif quis == 'stop':
        break
    

print(profs)