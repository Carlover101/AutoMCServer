import os
import time
import socket

vpsb = input("Would you like a 'Paper', 'Spigot', 'Bukkit', or 'Vanilla' Server? Choose 'Vanilla' if you don't know. ")

if vpsb == "Paper":
  os.system('wget -O PServer.jar "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/457/downloads/paper-1.16.5-457.jar"')
  jar = "PServer.jar"
  
elif vpsb == "Spigot":
  os.system('wget -O SServer.jar "https://getbukkit.org/get/RD0y91OTotryPrElNQe4ovBLDNweoO5Z"')
  jar = "SServer.jar"
  
elif vpsb == "Bukkit":
  os.system('wget -O BServer.jar "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar"')
  jar = "BServer.jar"
  
elif vpsb == "Vanilla":
  os.system('wget -O VServer.jar "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"')
  jar = "VServer.jar"
  
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
  YN = input("Would you like to Accept the EULA? (Yes/No/Help) ")

  if YN == "Yes":
    rf = open("EULA.txt","W+")
    
  elif YN == "No":
    really = input("Are you sure? (Yes/No) ")
    
    if really == "Yes":
      print("Aborting...")
      os.system(f"sudo rm {jar}")
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
      os.system(f"sudo rm {jar}")
      exit()

