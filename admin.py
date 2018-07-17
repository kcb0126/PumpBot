import requests
import compileall

baseurl = 'https://www.cluely.eu/'
#baseurl = 'http://localhost/pumpdump/'
verifyadminurl = baseurl + 'admin/verifyAdmin.php'
registerurl = baseurl + 'admin/register.php'
updateurl = baseurl + 'admin/updateUser.php'
changeadminurl = baseurl + 'admin/changeAdmin.php'
userlisturl = baseurl + 'admin/userlist.php'

def callapi(url, params):
    #debug = requests.post(url, params)
    data = requests.post(url, params).json()
    if data['success'] == 1:
        if 'data' in data:
            for row in data['data']:
                print(row)
        return True
    else:
        print(data['message'])
        return False

while True:
    print('[1] Login as administrator')
    print('[2] Quit')
    action = input()
    if action == '2':
        exit()
    elif action == '1':
        name = input('Input your name: ')
        password = input('Input your password: ')
        if not callapi(verifyadminurl, {'name':name, 'password':password}):
            continue
        else:
            while True:
                print('[1] Register a user.')
                print('[2] Update a user')
                print('[3] Change admin settings')
                print('[4] User list')
                print('[5] Back')
                action =input()
                if action == '1':
                    email = input('User\'s email: ')
                    pwd = input('User\'s password: ')
                    callapi(registerurl, {'name':name, 'password':password, 'email':email, 'pwd':pwd})
                elif action == '2':
                    email = input('User\'s email: ')
                    newemail = input('User\'s new email("" means no change): ')
                    pwd = input('User\'s password("" means no change): ')
                    refresh = input('Refresh device?(0=No | 1=Yes)')
                    params = {'name':name, 'password':password}
                    params['email'] = email
                    if newemail != '':
                        params['newemail'] = newemail
                    if pwd != '':
                        params['newpassword'] = pwd
                    if refresh == 1:
                        params['refresh'] = True
                    callapi(updateurl, params)
                elif action == '3':
                    newname = input('New name of administrator: ')
                    newpassword = input('New password of administrator: ')
                    callapi(changeadminurl, {'name':name, 'password':password, 'newname':newname, 'newpassword':newpassword})
                    name = newname
                    password = newpassword
                elif action == '4':
                    callapi(userlisturl, {'name':name, 'password':password})
                elif action == '5':
                    break
