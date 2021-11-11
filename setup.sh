#!/bin/bash

#install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/tahseenrahman/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

#install python 3
brew install python3
brew link python3

#install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

#install Django
pip3 install Django==3.2.8

#install node
brew install npm