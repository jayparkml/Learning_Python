# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

#JSON  :  JavaScript Object Notation

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)

  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]: # access as dictionary object
    print(theJSON["metadata"]["title"]) # access to title in metadata
    
  
  # output the number of events, plus the magnitude and each event name  
  count = theJSON["metadata"]["count"]
  print(str(count) + " events recorded")

  # for each event, print the place where it occurred
  for i in theJSON["features"]:
    print(i["properties"]["place"])
    print("--------------------------------------------\n")

  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 4.0:
      print("%2.1f" % i["properties"]["mag"], i["properties"]["place"]) #%2.1f formats a decimal with 2.1 spaces so 2 significant digits and one decimal
      print("--------------------------------------------\n")
    
  # print only the events where at least 1 person reported feeling something
  print("Events that were felt: ")
  for i in theJSON["features"]:
    feltreports = i["properties"]["felt"]
    if feltreports != None:
      if feltreports > 0:
        print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
        " reported " + str(feltreports) + " times")


def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode())) # need to get 200
  if (webUrl.getcode()==200):
    data = webUrl.read()
    printResults(data)
  else:
    print("Received error, cannot parse results")


if __name__ == "__main__":
  main()
