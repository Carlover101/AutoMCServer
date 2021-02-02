import os

if os.system('test -e "PServer.jar"') == "256":
  os.system('wget -O PServer.jar "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/457/downloads/paper-1.16.5-457.jar"')
  exit()
else:
  os.system("sudo rm PServer.jar")
  exit()
