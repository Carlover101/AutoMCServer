import os
import time
import socket

os.system("chmod +x ServerStart.sh")
vpsb = input("Would you like a 'Paper', 'Spigot', 'Bukkit', or 'Vanilla' Server? Choose 'Vanilla' if you don't know. ")

if vpsb == "Paper":
  os.system("python3 PServerInstall.py")
  jar = "PServerInstall.py"
  
elif vpsb == "Spigot":
  os.system("python3 SServerInstall.py")
  jar = "SServerInstall.py"
  
elif vpsb == "Bukkit":
  os.system("python3 BServerInstall.py")
  jar = "BServerInstall.py"
  
elif vpsb == "Vanilla":
  os.system("python3 VServerInstall.py")
  jar = "VServerInstall.py"
  
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
    rf = open("EULA.txt","W+")
    
  elif YN == "No":
    really = input("Are you sure? (Yes/No) ")
    
    if really == "Yes":
      print("Aborting...")
      os.system(f"python3 {jar}")
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
      os.system(f"python3 {jar}")
      exit()

EULA()
