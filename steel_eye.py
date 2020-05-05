import xml.etree.ElementTree as et 
import pandas as pd
import requests
from zipfile import ZipFile

mytree = et.parse("select.xml")
myroot = mytree.getroot()

filename = []
download_link = []

for child  in myroot [1]:
    for x in child:
        if x.attrib["name"] == "download_link":
            download_link.append(x.text)
        if x.attrib["name"] == "file_name":
            filename.append(x.text)

df  = pd.DataFrame({"File_Name": filename, 
                   "Download_Link": download_link})

df.to_csv("Data.csv", index=False)            

for index, row in df.iterrows():
    url = row["Download_Link"]
    resp = requests.get(url) 
    file_name = row["File_Name"]
    
    with open(file_name, 'wb') as f: 
        f.write(resp.content) 

  
    # opening the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 
      
        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall() 
        print('Done!')