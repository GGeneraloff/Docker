#!/bin/bash

cd ~/work/emulator/docker_install/
sudo chmod +x del_trei_nets
sudo ./del_trei_nets

cd ~/work/emulator/docker_install/
sudo chmod +x add_trei_nets
sudo ./add_trei_nets $1 $2 $3 $4

cp -nr ~/Docker/emulator/example_config_plc/default/run_emul_1 ~/work/emulator

cd ~/work/emulator
sudo chmod +x run_emul_1