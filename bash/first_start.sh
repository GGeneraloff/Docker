#!/bin/bash

sudo apt-get install -y docker*
cd ~
mkdir -p work
cp -nr ~/emulator/emulator ~/work
cd ~/work/emulator/container_emul/
sudo chmod +x restore
sudo ./restore