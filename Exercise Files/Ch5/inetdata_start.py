# 
# Example file for retrieving data from the internet
#

import urllib.request #http request

def main():
  webUrl = urllib.request.urlopen("http://www.google.com") # connect to website
  print("result code: "+ str(webUrl.getcode())) #200 if everything is ok
  data = webUrl.read() # read html code
  print(data)

if __name__ == "__main__":
  main()
