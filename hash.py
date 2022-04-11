import os;

dir= "/"


for filename in os.scandir(dir):
  if filename.is_file():
    print(filename.path)

