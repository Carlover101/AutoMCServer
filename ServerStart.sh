cd ~
cd Downloads
cd AutoMCServer-main
if test -e "PServer.jar"; then
  java -Xmx1024M -Xms1024M -jar PServer.jar nogui
if test -e "SServer.jar"; then
  java -Xmx1024M -Xms1024M -jar SServer.jar nogui
if test -e "BServer.jar"; then
  java -Xmx1024M -Xms1024M -jar BServer.jar nogui
if test -e "vServer.jar"; then
  java -Xmx1024M -Xms1024M -jar VServer.jar nogui
