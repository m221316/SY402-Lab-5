import os;
import hashlib

skip = ['/dev', '/proc', '/run', '/sys', 'tmp', '/var/lib', '/var/run']
dir= "/"
flag = 0

while(flag == 0):


  for filename in os.scandir(dir):
    if filename.is_file():
      f = open('files.txt', 'r')
      contents = f.read()
      f.close()
      if filename not in contents:
        
        f1 = open('files.txt', 'a')
        f1.write(filename + "\n")

  for name in os.scandir(dir):
    if os.path.isdir(name):
      dir = name
      
  

