from flask import Flask
from flask import request

import json

import numpy as np
import sys
def findMax(dataset):
    dataset = list(map(float, dataset))
    return max(dataset)
def findMin(dataset):
    dataset = list(map(float, dataset))
    return min(dataset)
def findAvg(dataset):
    dataset = list(map(float, dataset))
    dataset = list(map(float, dataset))
    return (sum(dataset))/(len(dataset))
def setupFile(fileName):
    global index
    file = open(fileName,"r")
    lines = (file.readlines())
    index={}
    dataNames=[]
    for i in range(len(lines)-1):

        
        lines[i] = lines[i].split(": ")

        lines[i][1] = (lines[i][1]).replace("\n","")
        lines[i][1]=lines[i][1].split()
    #    return(lines[i],lines[i][1])
        index[lines[i][0]] = lines[i][1]
        dataNames.append(lines[i][0])
    file.close()
    return lines

app = Flask(__name__);
@app.route('/deletedate',methods=['DELETE'])
def deletedate_api():
    data = request.json
    file = data["file"]
    date = data["date"]
    filen = setupFile(file)
    for time in date:
        place = (index["date"]).index(time)
        keys = list(index.keys())
        for key in keys:
            
            del index[key][place]
        fileAdd = open(file,"w")
        for key in keys:
            newLine = key+":"
            for item in index[key]:
                newLine += " "+item
            fileAdd.write(newLine+"\n")
        fileAdd.close()


    return "Data has been deleted"

@app.route('/getdata',methods=['GET'])
def getdata_api():
    returnData = ""
    data = request.json
    file = data["file"]
    date = data["date"]
    date2 = data["date2"]
    datapoints = data["variable"]
    filen = setupFile(file)

    for vari in datapoints:
        
        if date == date2:
            place = (index["date"]).index(date)
            returnData += ("The "+vari+" on "+str(date)+" was "+(index[vari])[place])+"\n"
        else:
            dateOne = date
            dateTwo = date2
            place1 = (index["date"]).index(dateOne)
            place2=(index["date"]).index(dateTwo)
            data= (index[vari])[place1:place2+1]
            returnData += ("The "+vari+" from "+str(dateOne)+" to "+str(dateTwo)+" was "+str(data))+"\n"
    return returnData

@app.route('/editdata',methods=['PUT'])
def editdata_api():
    data = request.json
    file = data["file"]
    date = data["date"]
    datapoints = data["variable"]
    replacements = data["value"]
    filen = setupFile(file)

    place = (index["date"]).index(date)
    keys = list(index.keys())
    for num in range(len(datapoints)):
        index[datapoints[num]][place] = replacements[num]
    fileAdd = open(file,"w")
    for key in keys:
        newLine = key+":"
        for item in index[key]:
            newLine += " "+item
        fileAdd.write(newLine+"\n")
    fileAdd.close()


    return "Data has been edited"
        
@app.route('/adddata',methods=['POST'])
def adddata_api():
    data = request.json
    file = data["file"]
    date = data["date"]
    weather_code = data["weather_code"]
    temperature_max = data["temperature_max"]
    temperature_min = data["temperature_min"]
    precipitation_sum = data["precipitation_sum"]
    wind_speed_max = data["wind_speed_max"]
    precipitation_probability_max = data["precipitation_probability_max"]
    
    
    filen = setupFile(file)


    

    for num in range(len(date)):
        keys = list(index.keys())
        
        

#yes
        keys.remove("date")
        #^
        
        index["date"].append(date[num])
        
        index["date"].sort()
        
        place = (index["date"]).index(date[num])

        
#?
        for key in keys:
            

            if key == "weather_code":
                inserted = weather_code[num]

            elif key == "temperature_max":
                inserted = temperature_max[num]
            elif key == "temperature_min":
                inserted = temperature_min[num]
            elif key == "precipitation_sum":
                inserted = precipitation_sum[num]
            elif key == "precipitation_sum":
                inserted = precipitation_sum[num]
            elif key == "wind_speed_max":
                inserted = wind_speed_max[num]
            elif key == "precipitation_probability_max":
                inserted = precipitation_probability_max[num]
            index[key].insert(place,inserted)

            #no
#no
        keys.insert(0,"date")
#no
        fileAdd = open(file,"w")



        for key in keys:
            newLine = key+":"
            for item in index[key]:
                newLine += " "+item
            fileAdd.write(newLine+"\n")
        fileAdd.close()


    return "Data has been edited"
        

    





