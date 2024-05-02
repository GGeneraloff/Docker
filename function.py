import os
import subprocess #для выполнения скриплов 

def first_start():
    try:
         docker_install=subprocess.run(["sudo apt-get install docker*"],capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    

def remove():
    docker_remove=subprocess.run(["sudo apt remove docker*"])

