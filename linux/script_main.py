#The os library is for running Bash commands in Python
import os
#The time library is for pauses in between commands
import time
#The socket library is for getting web information. In this case it's used for getting your computer's ip address to help you connect to the server.
import socket

def spformatter():
  os.system("python3 spformatter.py")

#These help to install or delete the server files.
class onedotsixteen():
  def paper():
    os.system("cd ~/AutoMCServer-linux/linux/1.16.5/")
    os.system("chmod +x P1.16.5.sh")
    os.system("./P1.16.5.sh")

  def spigot():
    os.system("cd ~/AutoMCServer-linux/linux/1.16.5/")
    os.system("chmod +x S1.16.5.sh")
    os.system("./S1.16.5.sh")
    
  def bukkit():
    os.system("cd ~/AutoMCServer-linux/linux/1.16.5/")
    os.system("chmod +x B1.16.5.sh")
    os.system("./B1.16.5.sh")
    
  def vanilla():
    os.system("cd ~/AutoMCServer-linux/linux/1.16.5/")
    os.system("chmod +x V1.16.5.sh")
    os.system("./V1.16.5.sh")

class onedotseventeen():
  def paper():
    os.system("cd ~/AutoMCServer-linux/linux/main/1.17.1/")
    os.system("chmod +x P1.17.1.sh")
    os.system("./P1.17.1.sh")

  def spigot():
    os.system("cd ~/AutoMCServer-linux/linux/1.17.1/")
    os.system("chmod +x S1.17.1.sh")
    os.system("./S1.17.1.sh")
    
  def bukkit():
    os.system("cd ~/AutoMCServer-linux/linux/1.17.1/")
    os.system("chmod +x B1.17.1.sh")
    os.system("./B1.17.1.sh")
    
  def vanilla():
    os.system("cd ~/AutoMCServer-linux/linux/1.17.1/")
    os.system("chmod +x V1.17.1.sh")
    os.system("./V1.17.1.sh")
#This makes the ServerStart.sh file executable.
os.system("chmod +x ServerStart.sh")

ver = input("What Minecraft version would you like? (1.16.5/1.17.1)")
#Lets you choose what type of server you want.
vpsb = input("Would you like a 'Paper', 'Spigot', 'Bukkit', or 'Vanilla' Server? Choose 'Vanilla' if you don't know. ")

#This helps to install the Paper version of Minecraft Servers.
if ver == "1.16.5":
  if vpsb.lower() == "paper":
    onedotsixteen.paper()
    jar = "paper"

  #This helps to install the Spigot version of Minecraft Servers.
  elif vpsb.lower() == "spigot":
    onedotsixteen.spigot()
    jar = "spigot"
    
  #This helps to install the Bukkit version of Minecraft Servers.
  elif vpsb.lower() == "bukkit":
    onedotsixteen.bukkit()
    jar = "bukkit"
    
  #This helps to install the Vanilla version of Minecraft Servers.
  elif vpsb.lower() == "vanilla":
    onedotsixteen.vanilla() 
    jar = "vanilla"
  
elif ver == "1.17.1":
  if vpsb.lower() == "paper":
    onedotseventeen.paper()
    jar = "paper"

  #This helps to install the Spigot version of Minecraft Servers.
  elif vpsb.lower() == "spigot":
    onedotseventeen.spigot()
    jar = "spigot"
    
  #This helps to install the Bukkit version of Minecraft Servers.
  elif vpsb.lower() == "bukkit":
    onedotseventeen.bukkit()
    jar = "bukkit"
    
  #This helps to install the Vanilla version of Minecraft Servers.
  elif vpsb.lower() == "vanilla":
    onedotseventeen.vanilla() 
    jar = "vanilla"

#Gets your computer ip address to help with connecting to the server later.
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

#Assigns your ip to a variable for use later.
ip = get_ip()

#Formats files for the Minecraft Server and Starts it.
def EULA():
  #Runs the bash script to generate the eula.txt file.
  os.system("./linux/ServerStart.sh")
  
  #Clears the terminal screen.
  os.system("clear")
  
  #Asks whether you want to accept the User License Agreement.
  YN = input("Would you like to Accept the EULA? (Yes/No/Help) ")

  #If you chose to accept the User License Agreement, then it will run this code.
  if YN == "Yes":
    
    #Opens the User License Agreement text file in write mode.
    rf = open("eula.txt","w+")
    
    #Re-writes the text inside of the User License Agreement file as to accept it.
    rf.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n")
    rf.write("eula=true")
    
    #Closes and saves the file.
    rf.close()
    
    #Prints the ip address of your computer that was collected earlier as to let you connect to the Minecraft Server.
    print(f"Type '{ip}' into the server address bar when the server has started.")
    time.sleep(3)
    print("Starting Server...")
    time.sleep(2)
    os.system("clear")
    
    #Re-runs the bash script as to start the Minecraft Server.
    os.system("./ServerStart.sh")

  #Runs this code if you chose not accept the User License Agreement.
  elif YN == "No":
    
    #Asks if you really want to not accept the agreement.
    really = input("Are you sure? (Yes/No) ")
    
    #If you really want to, then this code is run.
    if really == "Yes":
      print("Aborting...")
      
      #Checks which server type you chose and deletes it.
      if jar == "paper":
        onedotsixteen.paper()
        
      elif jar == "spigot":
        onedotsixteen.spigot()
        
      elif jar == "bukkit":
        onedotsixteen.bukkit()
        
      elif jar == "vanilla":
        onedotsixteen.vanilla()
        
      #Exits the script.
      exit()
    
    #If you chose to go back, then this code is run.
    elif really == "No":
      
      #Goes back to the top.
      EULA()
  
  #If you asked for help, then this code is run to give you information about the User License Agreement.
  elif YN == "Help":
    
    #Prints the contents of the eula.txt file.
    print(rf.readlines())
    time.sleep(2)
    
    #Asks if you want to go back to the top.
    c = input("Go back? (Yes/No) ")
    
    #If you chose yes, then it goes back.
    if c == "Yes":	
      EULA()
    
    #If you chose not to go back, then the program uninstalls the server files and exits the program.
    else:
      print("Aborting...")
      
      if jar == "paper":
        onedotsixteen.paper()
        
      elif jar == "spigot":
        onedotsixteen.spigot()
        
      elif jar == "bukkit":
        onedotsixteen.bukkit()
        
      elif jar == "vanilla":
        onedotsixteen.vanilla()
        
      exit()

format = input("Would you like to format the server.properties file? (yes/no/help) ").lower()

def frmt():
  if format == "yes":
    spformatter()
  elif format == "no":
    pass
  elif format == "help":
    input("The server.properties customizes how the server runs.")
    frmt()

#Runs the eula acceptance code.
EULA()
