if test -e "VServer.jar" &&; then
  sudo rm BServer.jar
fi

if test -e "VServer.jar" ||; then
  wget -O VServer.jar "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"
fi
