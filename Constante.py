import re
import os
from Encriptador import *
def IdentifyJSON(path,patron,secondPatron):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path=path.replace("/", r"\ ".strip())
        path=os.path.join(base_dir,path)
        content=open(f"{path}","r").read()
        
        patron=re.findall(f'{patron}' , content)
        patron=re.findall(f"{secondPatron}",patron[0])[0].split(":",2)[1].split(",",2)[0].strip()
        return patron
    except Exception as e:
        return ''

IV_B64 =       IdentifyJSON('appsetting.json',"other[\s|\S]+}",'"iv_b64": "[\S|" "|\\b]+"').replace('"', r'')
PASSPHRASE =   IdentifyJSON('appsetting.json',"other[\s|\S]+}",'"passphrase": "[\S|" "|\\b]+"').replace('"', r'')
ENCRYPT  =     IdentifyJSON('appsetting.json',"other[\s|\S]+}",'"encrypt": "[\S|" "|\\b]+"').replace('"', r'')

PATHCHROME =   IdentifyJSON('appsetting.json',"PathChrome[\s|\S]+}",'"value": "[\S|" "| |\\b]+"').replace('"', r'')
USER=          IdentifyJSON('appsetting.json',"User[\s|\S]+}",'"name": "[\S|" "|\\b]+"').replace('"', r'')
PASSWORDUSER = IdentifyJSON('appsetting.json',"User[\s|\S]+}",'"password": "[\S|" "|\\b]+"').replace('"', r'') if ENCRYPT=='True' else desencriptar(IV_B64,IdentifyJSON('appsetting.json',"User[\s|\S]+}",'"password": "[\S|" "|\\b]+"').replace('"', r''),PASSPHRASE)

SERVER =       IdentifyJSON('appsetting.json',"Mail[\s|\S]+}",'"server": "[\S|" "|\\b]+"').replace('"', r'')
PORT =         IdentifyJSON('appsetting.json',"Mail[\s|\S]+}",'"port": "[\S|" "|\\b]+"').replace('"', r'')
EMAIL =        IdentifyJSON('appsetting.json',"Mail[\s|\S]+}",'"email": "[\S|" "|\\b]+"').replace('"', r'')
PASSWORD =     IdentifyJSON('appsetting.json',"Mail[\s|\S]+}",'"password": "[\S|" "|\\b]+"').replace('"', r'')
TO =           IdentifyJSON('appsetting.json',"Mail[\s|\S]+}",'"to": "[\S|" "|\\b]+"').replace('"', r'')
