import os
import time
import socket

def paper():
  os.system('test -e PServer.jar && sudo rm PServer.jar || wget -O PServer.jar "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/457/downloads/paper-1.16.5-457.jar"')

def spigot():
  os.system('test -e "SServer.jar" && sudo rm SServer.jar || wget -O SServer.jar "https://getbukkit.org/get/RD0y91OTotryPrElNQe4ovBLDNweoO5Z"')
  
def bukkit():
  os.system('test -e "BServer.jar" && sudo rm BServer.jar || wget -O BServer.jar "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar"')
  
def vanilla():
  os.system('test -e "VServer.jar" && sudo rm VServer.jar || wget -O VServer.jar "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"')
  
os.system("chmod +x ServerStart.sh")

vpsb = input("Would you like a 'Paper', 'Spigot', 'Bukkit', or 'Vanilla' Server? Choose 'Vanilla' if you don't know. ")

if vpsb == "Paper":
  paper()
  jar = "paper"
  
elif vpsb == "Spigot":
  spigot()
  jar = "spigot"
  
elif vpsb == "Bukkit":
  bukkit()
  jar = "bukkit"
  
elif vpsb == "Vanilla":
  vanilla() 
  jar = "vanilla"
  
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        
    except Exception:
        IP = '127.0.0.1'
        
    finally:
        s.close()
        
    return IP

ip = get_ip()

def EULA():
  os.system("./ServerStart.sh")
  YN = input("Would you like to Accept the EULA? (Yes/No/Help) ")

  if YN == "Yes":
    rf = open("eula.txt","w+")
    rf.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).","\n","#Tue Feb 02 17:36:11 EST 2021","\n","eula=true")
    rf.close()
    os.system("./ServerStart.sh")
    
  elif YN == "No":
    really = input("Are you sure? (Yes/No) ")
    
    if really == "Yes":
      print("Aborting...")
      
      if jar == "paper":
        paper()
        
      elif jar == "spigot":
        spigot()
        
      elif jar == "bukkit":
        bukkit()
        
      elif jar == "vanilla":
        vanilla()
        
      exit()
      
    elif really == "No":
      EULA()
      
  elif YN == "Help":
    print("The EULA is the the Mojang user license agreement. It is required to continue.")
    time.sleep(2)
    c = input("Go back? (Yes/No) ")
    
    if c == "Yes":	
      EULA()
      
    else:
      print("Aborting...")
      
      if jar == "paper":
        paper()
        
      elif jar == "spigot":
        spigot()
        
      elif jar == "bukkit":
        bukkit()
        
      elif jar == "vanilla":
        vanilla()
        
      exit()

EULA()
