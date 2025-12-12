#!/data/data/com.termux/files/usr/bin/bash

pkg update -y
pkg install python git curl -y

rm -rf $HOME/IP-spam
mkdir -p $HOME/IP-spam
cd $HOME/IP-spam

curl -L -O https://raw.githubusercontent.com/boonkongbanpao-sudo/IP-spam/main/IP-spam.py

chmod +x IP-spam.py
python IP-spam.py
