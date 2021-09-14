## Welcome to the AutoMCServer Wiki!

You will find a more detailed desciption of the Automatic Minecraft Server project here.

### Index
[Installation](https://carlover101.github.io/AutoMCServer/#installation) | [Running the Script](https://carlover101.github.io/AutoMCServer/#running-the-starting-script) | [Installing Python](https://carlover101.github.io/AutoMCServer/#installing-python) | [Navigating the Script](https://carlover101.github.io/AutoMCServer/#navigating-the-starting-script) | [Troubleshooting and Issues](https://carlover101.github.io/AutoMCServer/#troubleshooting)

### Installation

1. Download the latest version from one of the links above or choose a specific version from the [project site](https://github.com/Carlover101/AutoMCServer/releases).
2. Open whichever files app you use and navigate to your Downloads folder.
3. Right-click the "AutoMCSever-main((.zip)or(.tar.gz))"
4. Extract the file:

- Zip file:
  - Look for an "extract" or "extract here" option.
  - If both of the options don't exist, open the terminal and type:

  ```
  cd ~/Downloads/
  unzip AutoMCServer-main.zip
  ```

  - If the "unzip" command is not recognized, then type this command and then retry the first two.

  ```
  sudo apt install unzip
  ```

- Tar file:
  - Look for an "extract" or "extract here" option.
  - If both of the options don't exist, open the terminal and type:

  ```
  cd ~/Downloads/
  tar --extract -xf AutoMCServer-main.tar.zf
  ```
  - And now you have succesfully installed (extracted) the package! All you have to do now is run the script.

### Running the Starting Script

1. If you haven't already done so, open your terminal.
2. Type cd ~/Downloads/AutoMCServer-main
3. Running the script:
   - If you have Python already installed, run:

   ```
   python3 main.py
   ```
   - If it is succesful, then skip to [Navigating the Starting Script](https://carlover101.github.io/AutoMCServer/#navigating-the-starting-script), otherwise try the steps below if Python is not installed.

### Installing Python

  - Type these commands in the terminal to download Python 3.6:

   ```
   sudo apt install software-properties-common
   sudo apt-add-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install python3.6
   ```

  - To install Python 3.8, if you so wish, type:

   ```
   sudo apt install software-properties-common
   sudo apt-add-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install python3.8
   ```

- Further docummentation provided at [this site](https://docs.python-guide.org/starting/install3/linux/)

- After the installation is complete, go back to [Running the Starting Script](https://carlover101.github.io/AutoMCServer/#running-the-starting-script)


### Navigating the Starting Script

1. First, after you have run the command the start the script, the terminal will prompt you to choose which Minecraft version you want. Currently only 1.16.5 and 1.17.1 are available.
2. Once you have chosen that, the terminal will prompt you to chose which server type you want. Currently: Paper, Spigot, Bukkit, and Vanilla.
3. Once you have chosen which one, the terminal will download the correct file and proceed to start the server to generate the "EULA.txt" file.
4. The terminal will then prompt you to accept the EULA (End user license agreement) found [Here](https://account.mojang.com/documents/minecraft_eula)
5. Once you have accepted, the terminal will start the server and give you the ip to type into the address bar on your Minecraft Client.
6. If nothing goes wrong, then the server will start.

### Troubleshooting

Problem: 
- Program errors out when trying to download jar files.

Solution:
- Make sure you extracted the zip or tar.gz file to your Downloads folder and not somwhere else.


#### Report a Problem [Here](https://github.com/Carlover101/AutoMCServer/issues)

- Expect an update as soon as possible, but just to be sure, you can turn on notifications for the project to get notified when there is an update.
