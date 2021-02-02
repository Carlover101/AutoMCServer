cd ~
cd Downloads
cd AutoMCServer-main
if test -e "PServer.jar"; then
  java -Xmx1024M -Xms1024M -jar PServer.jar nogui
fi

if test -e "SServer.jar"; then
  java -Xmx1024M -Xms1024M -jar SServer.jar nogui
fi

if test -e "BServer.jar"; then
  java -Xmx1024M -Xms1024M -jar BServer.jar nogui
fi

if test -e "VServer.jar"; then
  java -Xmx1024M -Xms1024M -jar VServer.jar nogui
fi
