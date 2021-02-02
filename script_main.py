import os
import time

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
