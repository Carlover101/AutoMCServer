import os

if os.system('test -e "SServer.jar"') == "256":
  os.system('wget -O SServer.jar "https://getbukkit.org/get/RD0y91OTotryPrElNQe4ovBLDNweoO5Z"')
  exit()
else:
  os.system("sudo rm SServer.jar")
  exit()
