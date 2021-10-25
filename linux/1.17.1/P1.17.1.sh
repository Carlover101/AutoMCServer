cd ~
cd AutoMCServer-main
clear

if [ -d "~/AutoMCServer-linux/linux/Minecraft_Server" ]
then
  cd Minecraft_Server
  if test -e "PServer-1.17.1.jar"
  then
    already="PServer-1.17.1.jar"
    read -r -p "You already have $already installed. Would you like to keep it? [Y/n] " input
    case $input in
        [yY][eE][sS]|[yY])
    echo "Okay"
    ;;
        [nN][oO]|[nN])
    echo "Deleting..."
    sleep 1s
    rm "PServer-1.17.1.jar"
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
    wget -O PServer-1.17.1.jar "https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/219/downloads/paper-1.17.1-219.jar"
    sleep 1s
    clear
    echo "Jar file download complete."
    sleep 1s
    clear
  fi
else
  mkdir Minecraft_Server
  cd Minecraft_Server
  if [ ! -d "~/AutoMCServer-linux/linux/Minecraft_Server"]
  then
    echo "Failed to create folder 'Minecraft_Server/'."
    sleep .5s
    echo "Do you have the neccesary permissions?"
  fi
  if test -e "PServer-1.17.1.jar"
  then
    already="PServer-1.17.1.jar"
    read -r -p "You already have $already installed. Would you like to keep it? [Y/n] " input
    case $input in
        [yY][eE][sS]|[yY])
    echo "Okay"
    ;;
        [nN][oO]|[nN])
    echo "Deleting..."
    sleep 1s
    rm "PServer-1.17.1.jar"
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
    wget -O PServer-1.17.1.jar "https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/219/downloads/paper-1.17.1-219.jar"
    sleep 1s
    clear
    echo "Jar file download complete."
    sleep 1s
    clear
  fi
  exit 1
fi
