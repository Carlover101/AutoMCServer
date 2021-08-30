cd ~
cd AutoMCServer13-main
clear

if [ -d "~/AutoMCServer-main/Minecraft_Server" ]
then
  cd Minecraft_Server
  if test -e "SServer-1.16.5.jar"
  then
    already="SServer-1.16.5.jar"
    read -r -p "You already have $already installed. Would you like to keep it? [Y/n] " input
    case $input in
        [yY][eE][sS]|[yY])
    echo "Okay"
    ;;
        [nN][oO]|[nN])
    echo "Deleting..."
    sleep 1s
    rm "SServer-1.16.5.jar"
    sleep 1s
    clear
    sleep .5s
    echo "Done"
          ;;
        *)
    echo "Invalid input..."
    exit 1
    ;;
    esac
  else
    echo "Preparing to install."
    sleep 2s
    clear
    wget -O SServer-1.16.5.jar "https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar"
    sleep 1s
    clear
    echo "Jar file download complete."
    sleep 1s
    clear
  fi
else
  mkdir Minecraft_Server
  cd Minecraft_Server
  if [ ! -d "~/AutoMCServer-main/Minecraft_Server"]
  then
    echo "Failed to create folder 'Minecraft_Server/'."
    sleep .5s
    echo "Do you have the neccesary permissions?"
  fi
  if test -e "SServer-1.16.5.jar"
  then
    already="SServer-1.16.5.jar"
    read -r -p "You already have $already installed. Would you like to keep it? [Y/n] " input
    case $input in
        [yY][eE][sS]|[yY])
    echo "Okay"
    ;;
        [nN][oO]|[nN])
    echo "Deleting..."
    sleep 1s
    rm "SServer-1.16.5.jar"
    sleep 1s
    clear
    sleep .5s
    echo "Done"
          ;;
        *)
    echo "Invalid input..."
    exit 1
    ;;
    esac
  else
    echo "Preparing to install."
    sleep 2s
    clear
    wget -O SServer-1.16.5.jar "https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar"
    sleep 1s
    clear
    echo "Jar file download complete."
    sleep 1s
    clear
  fi
  exit 1
fi
