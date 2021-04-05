## A take on the classic table-tennis-esque game, pong, written in modern python!

This is my take on the classic game, pong!
It's written in modern python (Python 3.9) and didn't take very long to make!

Right now it is missing a few features. Don't worry! I will be adding them very soon!

Features:
- The classic table-tennis-esque game, pong!

TODO:
- [ ] Main menu.
- [x] Fix background music.
- [ ] Bot/AI.
- [ ] Different modes/difficulties.

## Setup

Setup should be pretty simple, the commands below should set you up!

### Ubuntu (latested tested version is 18.04)
```sh
# Install python3.9 (requires ppa).
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9 python3.9-dev python3.9-distutils

# Install pip for 3.9.
wget https://bootstrap.pypa.io/get-pip.py
python3.9 get-pip.py && rm get-pip.py

# Clone pong.py from GitHub.
git clone https://github.com/yo-ru/pong.py.git && cd pong.py

# Install project requirements.
python3.9 -m pip install -r requirements.txt

# Run pong.py.
python3.9 pong.py
```

### Windows (latested tested version is 1909)
```sh
# Install python3.9.
1. Go to (https://www.python.org/downloads/release/python-391/) in your favorite browser.
2. Scroll down to the bottom and download your prefered 32-bit or 64-bit version of the Windows installer.
3. Open the installer.
4. Make sure "Install launcher for all users (recommended)" and "Add Python X.X to PATH" are both selected.
5. Click "Install Now".

# Clone pong.py from GitHub.
1. Open the Command Prompt.
2. Run "git clone https://github.com/yo-ru/pong.py.git && cd pong.py".

# Install project requirements.
1. Run "python -m pip install -r requirements.txt"

# Run pong.py.
1. Run "python pong.py"
```
