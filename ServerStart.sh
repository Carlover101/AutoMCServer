cd ~
cd AutoMCServer13
cd Minecraft_Server

if test -e "PServer-1.16.5.jar"; then
  java -Xmx1024M -Xms1024M -jar PServer-1.16.5.jar nogui
fi

if test -e "SServer-1.16.5.jar"; then
  java -Xmx1024M -Xms1024M -jar SServer-1.16.5.jar nogui
fi

if test -e "BServer-1.16.5.jar"; then
  java -Xmx1024M -Xms1024M -jar BServer-1.16.5.jar nogui
fi

if test -e "VServer-1.16.5.jar"; then
  java -Xmx1024M -Xms1024M -jar VServer-1.16.5.jar nogui
fi

if test -e "PServer-1.17.1.jar"; then
  java -Xmx1024M -Xms1024M -jar PServer-1.17.1.jar nogui
fi

if test -e "SServer-1.17.1.jar"; then
  java -Xmx1024M -Xms1024M -jar SServer-1.17.1.jar nogui
fi

if test -e "BServer-1.17.1.jar"; then
  java -Xmx1024M -Xms1024M -jar BServer-1.17.1.jar nogui
fi

if test -e "VServer-1.17.1.jar"; then
  java -Xmx1024M -Xms1024M -jar VServer-1.17.1.jar nogui
fi
