## Welcome to the AutoMCServer Wiki!

You will find a more detailed desciption of the Automatic Minecraft Server project here.

### Index
[Installation](https://carlover101.github.io/AutoMCServer/#installation)

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
     python3 script_main.py
     ```
   - If it is succesful, then skip to [Navigating the Starting Script](https://carlover101.github.io/AutoMCServer/#navigating the starting script), otherwise try the steps below if Python is not installed.

#### Installing Python

1. Copy this link into a new tab to go to the Python downloads page: https://python.org/downloads/source
2. Choose the preferred version (over 3.5) and download it.
3. If you have not already done so, open your terminal and type:
   ```
   cd ~/Downloads/
   tar --extract -xf Python-3.(whichever version you chose).tar.gz
   cd Python-3.(Whichever version you chose)/
   ./configure
   sudo make test
   sudo make install
   ```
   - After the installation is complete, go back.


### Navigating the Starting Script
