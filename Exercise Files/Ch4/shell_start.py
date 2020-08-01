#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive #shellutility
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    dst = src+ ".bak"
    
    # copy over the permissions, modification times, and other info
    # shutil.copy(src, dst) # copy the content
    # shutil.copystat(src, dst) #  copies metadata like modified time

    # rename the original file
    # os.rename("textfile.txt", "newfile.txt")
    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(src) #tail : textfile.txt
    # shutil.make_archive("archive", "zip", root_dir)
    # print(tail)
    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
      newzip.write("textfile.txt")
      newzip.write("textfile.txt.bak")

      
if __name__ == "__main__":
  main()
