if test -e "PServer.jar" &&; then
  sudo rm PServer.jar
fi

if test -e "PServer.jar" ||; then
  wget -O PServer.jar "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/457/downloads/paper-1.16.5-457.jar"
fi
