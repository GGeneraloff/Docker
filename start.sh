#!/bin/bash

cd ~/work/emulator/docker_install/
sudo chmod +x del_trei_nets
sudo ./del_trei_nets

cd ~/work/emulator/docker_install/
sudo chmod +x add_trei_nets
 $1 $2 $3 $4
sudo ./add_trei_nets
cp -nr ~/Docker/emulator/example_config_plc/default/run_emul_1 ~/work/emulator
cp -nr ~/Docker/emulator/example_config_plc/default/run_emul_2 ~/work/emulator
cp -nr ~/Docker/emulator/example_config_plc/default/run_emul_3 ~/work/emulator
cp -nr ~/Docker/emulator/example_config_plc/default/run_emul_4 ~/work/emulator
cd ~/work/emulator
sudo chmod +x run_emul_1
sudo chmod +x run_emul_2
sudo chmod +x run_emul_3
sudo chmod +x run_emul_4

sudo ./run_emul_1 $1
# sudo ./run_emul_2
# sudo ./run_emul_3
# sudo ./run_emul_4

# sudo docker stop trei_emul_11

