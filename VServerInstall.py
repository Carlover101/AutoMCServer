import os

if os.system('test -e "VServer.jar"') == "256":
  os.system('wget -O VServer.jar "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"')
  exit()
else:
  os.system("sudo rm VServer.jar")
  exit()
