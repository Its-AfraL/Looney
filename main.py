# Current Looney version : v1.3

# </> The world is our


# Looney is a marketing tool made for EDUCATIONNAL PURPOSE ONLY
# Don't forget that this script is for educationnal purpose only, you must not use this script for illegal business but for a marketing goal or for educationnal purpose only, do not send sms to someone who didn't allow you to promote your product to him. You can use this script to contact your customers who allow you to sms them !
# Do not forget that at any moment a customer can tell you to stop sending him sms !
# We will not be responsible of what you will do with this powerful tool !


# Importing dependencies and sources scripts made by us
# All premade script are created by us, you can find them in the source folder
# Source folder : src/

from src.headers import generate_header
from pyfade import Fade, Colors
from src.list_gen import generate_num_list
from src.sender import message_send, setting_up
from src.contact_gen import contact_generator
import os
import time
import random
import string
import AutoUpdate

looney_version = "1.3"

def auto_update_looney():
    
    os.system("cls")
    os.system("title AfraL © 2022  x  Looney ^| v1.3")
    print(Fade.Vertical(Colors.black_to_white, generate_header()))
    
    print(f'\n[*]Actual Looney version : v{looney_version} checking for Looney new updates...')
    
    AutoUpdate.set_url("https://raw.githubusercontent.com/Its-AfraL/looney_version/main/version.txt?token=GHSAT0AAAAAABXZA6HCGXBEJUMRUWNA7I2SYX6JRGA")
    AutoUpdate.set_current_version(str(looney_version))

    up_to_date = AutoUpdate.is_up_to_date()
    
    if up_to_date == True:
        print("[+] Looney is up to date !") 
        
        print("\n[*] Starting the script...")
        time.sleep(2)
        interface()
    
    else if up_to_date == False:
        print("[-] A new version of Looney has been uploaded")
        print("[*] Looney will auto-update..."\)
        
	

global choice


def interface():
    # Printing the banner

    os.system("cls")
    os.system("title AfraL © 2022  x  Looney ^| v1.3")
    print(Fade.Vertical(Colors.black_to_white, generate_header()))

    # Printing differents choice

    print("\n   /!\ This script is made for educationnal purpose only /!\ \n\n")
    print("1 > Generate num list with indicator(s) ")
    print("2 > SMS a num list ")
    print("3 > Generate a .vcf contacts file ")
    print("\n4 > Tutorial ")

    choice = input("\n>>> ")

    try:
        choice = int(choice)
        print(choice)
    except:
        interface()

    return choice


def sms_num():

    # This function is a function to mass promote a list of customers WHO ARE OKAY TO RECEIVE PROMOTION MESSAGES, DON'T FORGET THAT SPAMMING PEOPLES WHO ARE NOT OKAY IS ILLEGAL !

    os.system("cls")

    print(Fade.Vertical(Colors.black_to_white, generate_header()))
    print("\n")
    os.system("dir /b src\lists")
    print("\n")
    list_name = input("Please enter list name >>> ")

    try:
        pwd = os.getcwd()
        path_list = "src\lists" + "\\" + list_name

        list = open("src\lists" + "\\" + list_name)

    except:
        print("\n >> Fichier invalide")
        time.sleep(3)
        sms_num()

    # IOS = trash
    # Never forget it ;)

    android_ip = input("Please enter your android ip adress>>> ")
    message_to_send = input("Please enter the message to send >>> ")

    setting_up(list_path=path_list)
    message_send(def_ip=android_ip, message=message_to_send,
                 list_path=path_list)

    # You will need to unleash your android phone in order to send a mass quantity of messages


def generate_list():

    # This is a function to create a list with all possibility of France phones numbers
    # Do not send a message to peoples in these lists if they are not okay with your promotion
    # You can choose indicators you want to admit in your lists !

    os.system("cls")

    print(Fade.Vertical(Colors.black_to_white, generate_header()))
    print("\n")

    def_indicatifs = str(
        input("Please enter below phone's indicatives (06,07...) >>> "))
    raw_list_name = str(input("Please enter below list name >>> "))
    def_list_name = "output\lists\\" + raw_list_name

    print("\n")

    # All generated lists are in the output folder !
    # Output folder : output/

    generate_num_list(indicatifs=def_indicatifs, list_name=def_list_name)
    print(f">>> List generated in output/lists/{raw_list_name}.txt")

    os.system("pause>nul")
    choice()


def tutorial():

    # Only print, i will add argparse arguments !

    os.system("cls")

    print(Fade.Vertical(Colors.black_to_white, generate_header()))
    print("\n")
    print("How to generate a num list ?")
    print("\n")
    print("Use the first function of the script from the main menu, type your indicatives in this format : 06,07 and a list output name, the list will be generate in src/lists")

    print("\n")
    print("How to begin an attack ?")
    print("\n")
    print("Use the second function of the script from the main menu, select your num list and then connect the Airmore Session on the Android equiped with a sim card to start the attack")

    print("\n")
    print("How to connect an Airmore Session  ?")
    print("\n")
    print("For this you will need to install Airmore on your Android phone (playstore) and then enter in the app follow the steps to allow the rights to send message and then click on the top right button : \"Get IP adress\", make sure the devices are on the same WiFi and copy paste the IP on lLooney pannel, then just accept the connection request and let the script make it work.")

    os.system("pause>nul")
    choice()


def contact_gen():

    # Contact Generator is a function made by AfraL to create a .vcf file from a raw text file which contains phone numbers in this format : 06 ** ** ** **
    # Don't forget that this script is for educationnal purpose only, you should not use this script for illegal business but for a marketing goal or for educationnal purpose
    # We will not be responsible of what you will do with this powerful tool !

    os.system("cls")

    print(Fade.Vertical(Colors.black_to_white, generate_header()))
    print("\n")
    os.system("dir /b src\lists")
    print("\n")
    list_name = input("Please enter list name >>> ")

    try:
        pwd = os.getcwd()
        path_list = "src\lists" + "\\" + list_name

        list = open("src\lists" + "\\" + list_name)

    except:
        print("\n >> Fichier invalide")
        time.sleep(3)
        contact_gen()

    raw_list_name = str(input("Please enter below list name >>> "))
    def_list_name = "output\contacts\\" + raw_list_name

    contact_generator(list=path_list, output=def_list_name)

    #print(raw_list_name)
    print(f"\n>>> List generated in output/contacts/{raw_list_name}.vcf")

    os.system("pause>nul")
    choice()


def choice():
    choice = interface()

    if choice == 1:
        generate_list()

    elif choice == 2:
        sms_num()

    elif choice == 4:
        tutorial()

    elif choice == 3:
        contact_gen()

    else:
        interface()


choice()