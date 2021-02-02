if test -e "BServer.jar" &&; then
  sudo rm BServer.jar
fi

if test -e "BServer.jar" ||; then
  wget -O BServer.jar "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar"
fi
