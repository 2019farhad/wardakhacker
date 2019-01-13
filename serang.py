#!/usr/bin/python



import requests,json,time,subprocess
import os, time
import subprocess as sp

subprocess.call("clear", shell=True)

banner = """
╔╗╴╴╴╔══════╗ 
║╚═══╝╴╚════╗ 
╚════╗╴╔═══╗║ 
╔════╝╴║╴╴╴║║ 
╚══════╝╴╴╴╚╝
"""

x = 0
print banner
a = raw_input("[+] Lanjutkan (y/n): ")
d = raw_input("[+] Jumlah : ")
while x < d:
   b = {"https://xxnx.com":a}
   c = " https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor=6281344772900"
   e = requests.post(c, data=b)
   f = json.loads(e.text)
   if "nexmo_request_id" in f:
       print "[+] SUCESS WITH ID",f["nexmo_request_id"]
   else:
       print "[+] Spam Succes"
