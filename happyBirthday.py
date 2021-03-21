# pip install pyfiglet
import pyfiglet
import time
import os

import termios
import struct
import fcntl
os.system('cls' if os.name == 'nt' else 'clear')



#import subprocess

#subprocess.Popen(["mode", "con:", "cols=50", "lines=80"])


ascii_banner = pyfiglet.figlet_format("Hello Vaiva.... \n")
print(ascii_banner)
time.sleep(3)
ascii_banner = pyfiglet.figlet_format("               This is your friend (Python 3)...")
print(ascii_banner)
time.sleep(3)
ascii_banner = pyfiglet.figlet_format("\n speaking from beyond the silicon....")
print(ascii_banner)
time.sleep(3)
ascii_banner = pyfiglet.figlet_format("\n I have a sexy surprise for you...")
print(ascii_banner)
time.sleep(3)

os.system('cls' if os.name == 'nt' else 'clear')

art='./art2'
f=open(art,'r')
for line in f:
	print(line)
f.close()	
	
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


art='./art'
f=open(art,'r')
for line in f:
	print(line)
f.close()	

	
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


art='./art3'
f=open(art,'r')
for line in f:
	print(line)
f.close()	
