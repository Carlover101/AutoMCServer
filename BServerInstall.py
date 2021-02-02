import os

if os.system('test -e "BServer.jar"') == "256":
  os.system('wget -O BServer.jar "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar"')
  exit()
else:
  os.system("sudo rm BServer.jar")
  exit()
