import time
from datetime import datetime as dt

host_temp="hosts"
hostpath= r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.chess.com","chess.com","www.facebook.com"]


while True:
    if (dt(dt.now().year,dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day,15)):
        print("you have to study bro")
        with open(hostpath,'r+') as file:
            content=file.read()
            for website in website_list:
                if not (website in content):                    
                    file.write("\n"+ redirect+ " " + website + "\n")


    else:
        with open(hostpath,'r+') as file:
            content= file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

                file.truncate()
        print("its fun time man...")
    time.sleep(5)