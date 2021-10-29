version=$(python3 --version)
echo $version
version=$(tr -dc '.0-9' <<< $version)
basenum="3.6"
if [[ $version < $basenum && true ]]; then
  sudo apt install software-properties-common
  sudo apt-add-repository ppa:deadwolves/ppa
  sudo apt update
  sudo apt install python 3.10
  cd ~
  echo -e '\nalias python3="/usr/bin/python3.10"' >> .bashrc
  source .bashrc
  bash -l
fi
