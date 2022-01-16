#Imports CSV read and JSON write functions
import csv
import json

#Adjust CSV filename as needed
with open('Roster.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    #Loops through CSV rows, each containing a single token's characteristics
    for row in csv_reader:
        
        #Option if statement to process only certain tokens if desired
        if line_count >= 0:
            line_count += 1
        
            #IPFS CAR pin for token collection images
            archive = "ipfs://bafybeiatmiig6ylhha5p7o7bxvqutfitv6k2n5ghche4r22tgkmoz6gu5u/"

            #Create a variable for each token trait
            filename = row[0]
            name = row[1]
            park = row[2]
            type = row[3]
            feature = row[4]

            #Convert the variables into JSON format
            NFTjson = {"name":name,"description":"Pics from parks around the world.","image":archive+filename+".png","properties":{"Park":park,"Type":type,"Feature":feature}}
            
            #Translate into a string, create a new JSON with a name matching the token ID, write the JSON, and save the JSON
            jsonString = json.dumps(NFTjson)
            jsonFile = open(filename+".json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
        else:
            line_count += 1
    #Optional tracker to confirm completion
    print(f'Processed {line_count} lines.')