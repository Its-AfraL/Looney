from ipaddress import IPv4Address
from itertools import count
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
import os
import datetime
import time
from src.headers import generate_header
from pyfade import Fade, Colors

global num_number
num_number = 0


def setting_up(list_path):
    count = open(str(list_path), "r")
    text = count.readlines()
    num_number = 1000


def message_send(def_ip, message, list_path):

    try:
        ip = IPv4Address(def_ip)

        session = AirmoreSession(ip)
        service = MessagingService(session)

    except:
        exit()

    message_sent = 0
    erreurs = 0

    list = open(list_path, "r")
    start = time.time()
    print("\n>>> Ready, press any key to start the attack")

    os.system("pause>nul")

    os.system("cls")
    print(Fade.Vertical(Colors.black_to_white, generate_header()))

    for num in list:
        try:
            service.send_message(num, message)
            message_sent += 1

        except MessageRequestGSMError:
            erreurs += 1

        curr_time = str(
            datetime.timedelta(seconds=(time.time() - start))
        ).split(".")[0]

        os.system(
            f"title AfraL © 2022  x  Looney ^| {message_sent}/{num_number} ^| Errors : {erreurs} ^| Elapsed Time: {curr_time} ^| v1.3"
            if os.name == "nt"
            else ""
        )
        time.sleep(1)
