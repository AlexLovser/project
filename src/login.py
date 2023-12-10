import json



def open_db():
    with open('./database.json', 'r') as f:
        return json.load(f)
    
def commit_db(data):
    with open('./database.json', 'w') as f:
        return json.dump(data, f)




def auth():
    s = True
    while s:
        quis = input('Do u have profile here (y/n) or "stop": ')
        if quis == 'y':
            print('*****LOGIN SCREEN*****')
            nickname = input("Entrez ton NickName : ")
            password = input("Entrez ton Password : ")
            profiles = open_db()
            if nickname in profiles:
                if profiles[nickname]['password'] == password :
                    s = False
                    return nickname
                else:
                    print("The password is invalid")
            else :
                print("Current user does not exist")
        elif quis == 'n' :
            print('*****SING UP SCREEN*****')
            nickname = input("Entrez ton NickName : ")
            password = input("Entrez ton Password : ")

            profiles = open_db()
            if nickname not in profiles:
                profiles[nickname] = {
                    'password': password,
                    'games': [
                        {
                            'disk_number': 5,
                            'ideal': 17,
                            'score': 23,
                            'win': False,
                            'time': 123,
                            'solution_used': False
                        }
                    ]
                }

                commit_db(profiles)
                print("Done!")
                return nickname
                
            else :
                print("Profiles with this nickname already exists")
        elif quis == 'stop':
            s = False
        


def get_diificulty():
    i = input('Enter the level of difficulty (from 1 till 6): ')
    try:
        i = int(i)

        if 6 >= i >= 1:
            return i
        
        print('Invalid! The level can only be a number between 1 and 6!')
        return get_diificulty()
    except:
        print('Invalid!')
        return get_diificulty()