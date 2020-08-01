#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("textfile.txt", "w+") # w:write +:create when not exist



  # Open the file for appending text to the end
  f = open("textfile.txt", "r") # a: append data not overwriting
                                # r: read

  # write some lines of data to the file
  # for i in range(10):
  #   f.write("This is line " + str(i) + "\r\n") 
# \r (Carriage Return) → moves the cursor to the beginning of the line without advancing to the next line
# \n (Line Feed) → moves the cursor down to the next line without returning to the beginning of the line — In a *nix environment \n moves to the beginning of the line.
# \r\n (End Of Line) → a combination of \r and \n
  
  # close the file when done
  # f.close()
  
  # Open the file back up and read the contents
  if f.mode == "r": # check file opend in read mode
    fl = f.readlines()
    for x in fl:
      print(x)
    # content = f.read()
    # print(content)
    
if __name__ == "__main__":
  main()
