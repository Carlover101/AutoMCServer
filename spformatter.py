import time

print("The Server.properties file changes how the server runs and generates worlds.")
time.sleep(2)
YD = input("Would you like to customize this file or leave it as the default values? (Custom/Default)")

if YD.lower() == "Default":
  print("Setting to default...")
  time.sleep(1)
  print("Done")
  exit()
elif YD.lower() == "Custom":
  ejmxmon = input("Enable jmx monitoring? (True/False)").lower()
  rconport = input("What should the rcon port be default is 25575 ")
  lvlseed = input("What should the level seed be? (Leave blank if random is wanted)")
  
sp = open("server.properties","w+")

sp.write("#Minecraft server properties\n")
sp.write(f"enable-jmx-monitoring={ejmxmon}\n")
