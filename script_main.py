import os
import time
import socket

vpsb = input("Would you like a 'Paper', 'Spigot', 'Bukkit', or 'Vanilla' Server? Choose 'Vanilla' if you don't know.")

os.system("sudo mkdir ~/MCServer")

if vpsb == "Paper":
  os.system('wget -O PServer.jar "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/457/downloads/paper-1.16.5-457.jar" -P ~/MCServer')
  
elif vpsb == "Spigot":
  os.system('wget -O SServer.jar "https://getbukkit.org/get/RD0y91OTotryPrElNQe4ovBLDNweoO5Z" -P ~/MCServer')

elif vpsb == "Bukkit":
  os.system('wget -O BServer.jar "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar" -P ~/MCServer')
  
elif vpsb == "Vanilla":
  os.system('wget -O VServer.jar "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar" -P ~/MCServer')

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

os.system("cd ~")
os.system("cd MCServer")
