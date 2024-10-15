#Weather Project Main File
#Started on 5/24/24 by Arjun Rajaram

import requests
import json
#FIXES / TODOS:
#1. Change the list slices to include one past what they already do based on directions

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
#Finish weather decoder later, should probably just use a dictionary for it if I have time.
def weatherDecoder(code):
    if code == 0:
        return ("Clear Sky")
def createHistogram(items,vari,start,end):
    length = []
    count = 0
    for i in range(start, end+1):
        length.append(i)
        items[count] = (float(items[count]))

        count+=1

        
                   
    x = np.array(length)
    y = np.array(items)
    plt.xticks(np.arange(min(length),max(length)+1, 1))  
    plt.yticks(np.arange(0, round(max(items))+1, 1))
    plt.xlabel("Day #")
    plt.ylabel(str(vari))
    plt.title(str(vari)+" over "+str(len(length))+" days")
    plt.bar(x,y,edgecolor='black')
    print("Your graph is being created. Make sure to close it before entering another command!")
    plt.show()
    

import matplotlib.pyplot as plt
import numpy as np
import sys

while True:
    print('Please enter the pathway of the file that is to be used. (This can be found by searching the file name and clicking "Copy Path") If you want to quit the program, input "Quit".')
    location = input()
    if location.lower() == "quit":
        sys.exit("Thank you for using this application!")
        quit()
    try:
        file = open(location,"r")
    except:
        print("Oops! It seems that pathway didn't work. Please make sure the file exists, and that you are copying the pathway based on the instructions above.\n")
    else:
        lines = (file.readlines())
        break

index={}
dataNames=[]
for i in range(len(lines)-1):

    
    lines[i] = lines[i].split(": ")

    lines[i][1] = (lines[i][1]).replace("\n","")
    lines[i][1]=lines[i][1].split()
#    print(lines[i],lines[i][1])
    index[lines[i][0]] = lines[i][1]
    dataNames.append(lines[i][0])
#    print(index[lines[i][0]])
print("That pathway worked!")
while True:
    print('Enter what data you want to see, or enter "Quit" to exit the program.')
    command = input().split()
    if command[0].lower() == "quit":
        sys.exit("Thank you for using this application!")
    if (command[0]).lower() == "what":
        vari = command[3]
        if len(command) == 6:
            date = command[5]
            place = (index["date"]).index(date)
            print("The "+vari+" on "+str(date)+" was "+(index[vari])[place])
        else:
            date = int(command[6])
            print("The "+vari+" on day "+str(date)+" was "+(index[vari])[date])
    elif command[0].lower() == "create":
        if len(command) == 11:
            vari = command[4]
            dateOne = int(command[7])
            dateTwo = int(command[10])
            data= (index[vari])[dateOne:dateTwo+1]
            createHistogram(data,vari,dateOne,dateTwo)
        else:
            vari = command[4]
            dateOne = (command[6])
            dateTwo = (command[8])
            place1 = (index["date"]).index(dateOne)
            place2=(index["date"]).index(dateTwo)
            data= (index[vari])[place1:place2+1]
            createHistogram(data,vari,place1,place2)
#The numbers of compare will have to change if I confirm the format and it is not like I thought. I'll assume its “Compare the wind_speed_max on 2024-04-24 at 41.2565 and -95.9345” for right now
    elif command[0].lower() == "compare":
        url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=weather_code&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&start_date=2024-04-11&end_date=2024-08-11'
        if 'days' in command or 'day' in command:
            if len(command) == 12:
                latitude = "latitude="+command[8]
                longitude = "longitude="+command[11]
                url = url.replace('latitude=52.52',(latitude))
                url = url.replace('longitude=13.41',(longitude))
                date = int(command[5])
                
                place = (index["date"])[date]


                
                startDate = "start_date="+place

                endDate = "end_date="+place

                url = url.replace("start_date=2024-04-11",startDate)
                url = url.replace("end_date=2024-08-11",endDate)
                maxi = command[2].lower()
                dataPoint = command[2]
                if dataPoint == "weather_code":
                    dataPoint = "weather_code"
                elif dataPoint == "temperature_max":
                    dataPoint = "temperature_2m_max"
                elif dataPoint == "temperature_min":
                    dataPoint = "temperature_2m_min"
                elif dataPoint == "precipitation_sum":
                    dataPoint = "precipitation_sum"
                elif dataPoint == "wind_speed_max":
                    dataPoint= "wind_speed_10m_max"
                elif dataPoint == "precipitation_probability_max":
                    dataPoint = "precipitation_probability_max"
                url = url.replace("weather_code",dataPoint)
                response = requests.get(url)
                data = response.text
                res = json.loads(data)


                place = (index["date"]).index(place)
                if dataPoint == "precipitation_probability_max":
                    
                    print("In the given data the "+str(command[2])+" was "+str((index[command[2]])[place])+"%"+" while at latitude "+str(command[6])+" and longitude "+str(command[8])+" it was "+(str(res["daily"][dataPoint][0])+"%"))  
                else:
                    
                    print("In the given data the "+str(command[2])+" was "+str((index[command[2]])[place])+" "+res["daily_units"][dataPoint]+" while at latitude "+str(command[6])+" and longitude "+str(command[8])+" it was "+(str(res["daily"][dataPoint][0])+" "+res["daily_units"][dataPoint]))
            elif len(command) ==16:
                latitude = "latitude="+command[12]
                longitude = "longitude="+command[15]
                url = url.replace('latitude=52.52',(latitude))
                url = url.replace('longitude=13.41',(longitude))
                date = int(command[6])
                date2 = int(command[9])
                
                place = (index["date"])[date]
                place2 = (index["date"])[date2]


                
                startDate = "start_date="+place

                endDate = "end_date="+place2

                url = url.replace("start_date=2024-04-11",startDate)
                url = url.replace("end_date=2024-08-11",endDate)
                
                dataPoint = command[3]
                maxi = command[2]
                if dataPoint == "weather_code":
                    dataPoint = "weather_code"
                elif dataPoint == "temperature_max":
                    dataPoint = "temperature_2m_max"
                elif dataPoint == "temperature_min":
                    dataPoint = "temperature_2m_min"
                elif dataPoint == "precipitation_sum":
                    dataPoint = "precipitation_sum"
                elif dataPoint == "wind_speed_max":
                    dataPoint= "wind_speed_10m_max"
                elif dataPoint == "precipitation_probability_max":
                    dataPoint = "precipitation_probability_max"
                url = url.replace("weather_code",dataPoint)

                response = requests.get(url)
                data = response.text
                res = json.loads(data)

                placeStart = (index["date"]).index(place)
                placeEnd = (index["date"]).index(place2)
                oldData = (index[command[3]])[placeStart:placeEnd+1]
                if maxi == 'maximum':
                    chosen = findMax(res["daily"][dataPoint])
                    oldChosen = findMax(oldData)
                elif maxi == 'minimum':
                    chosen = findMin(res["daily"][dataPoint])
                    oldChosen = findMin(oldData)
                elif maxi == 'average':
                    chosen = findAvg(res["daily"][dataPoint])
                    oldChosen = findAvg(oldData)


                lessThan = "equal to"
                if float(oldChosen) < chosen:
                    lessThan = "less than"
                elif float(oldChosen) > chosen:
                    lessThan = "greater than"

                if dataPoint == "precipitation_probability_max":
                    print("The "+maxi+" "+command[3]+" from days "+str(date)+" to "+str(date2)+" was "+str(oldChosen)+"%"+" which is "+lessThan+ " "+str(chosen)+"%"+" at latitude "+command[12]+" longitude "+command[15])


                else:
                    

                    print("The "+maxi+" "+command[3]+" from days "+str(date)+" to "+str(date2)+" was "+str(oldChosen)+" "+res["daily_units"][dataPoint]+" which is "+lessThan+ " "+str(chosen)+" "+res["daily_units"][dataPoint]+" at latitude "+command[12]+" longitude "+command[15])

            elif len(command) == 15:
                latitude = "latitude="+command[11]
                longitude = "longitude="+command[14]
                url = url.replace('latitude=52.52',(latitude))
                url = url.replace('longitude=13.41',(longitude))
                date = int(command[6])
                date2 = int(command[8])
                
                place = (index["date"])[date]
                place2 = (index["date"])[date2]


                
                startDate = "start_date="+place

                endDate = "end_date="+place2

                url = url.replace("start_date=2024-04-11",startDate)
                url = url.replace("end_date=2024-08-11",endDate)
                
                dataPoint = command[3]
                maxi = command[2]
                if dataPoint == "weather_code":
                    dataPoint = "weather_code"
                elif dataPoint == "temperature_max":
                    dataPoint = "temperature_2m_max"
                elif dataPoint == "temperature_min":
                    dataPoint = "temperature_2m_min"
                elif dataPoint == "precipitation_sum":
                    dataPoint = "precipitation_sum"
                elif dataPoint == "wind_speed_max":
                    dataPoint= "wind_speed_10m_max"
                elif dataPoint == "precipitation_probability_max":
                    dataPoint = "precipitation_probability_max"
                url = url.replace("weather_code",dataPoint)

                response = requests.get(url)
                data = response.text
                res = json.loads(data)

                placeStart = (index["date"]).index(place)
                placeEnd = (index["date"]).index(place2)
                oldData = (index[command[3]])[placeStart:placeEnd+1]
                if maxi == 'maximum':
                    chosen = findMax(res["daily"][dataPoint])
                    oldChosen = findMax(oldData)
                elif maxi == 'minimum':
                    chosen = findMin(res["daily"][dataPoint])
                    oldChosen = findMin(oldData)
                elif maxi == 'average':
                    chosen = findAvg(res["daily"][dataPoint])
                    oldChosen = findAvg(oldData)


                lessThan = "equal to"
                if float(oldChosen) < chosen:
                    lessThan = "less than"
                elif float(oldChosen) > chosen:
                    lessThan = "greater than"

                if dataPoint == "precipitation_probability_max":
                    print("The "+maxi+" "+command[3]+" from days "+str(date)+" to "+str(date2)+" was "+str(oldChosen)+"%"+" which is "+lessThan+ " "+str(chosen)+"%"+" at latitude "+command[11]+" longitude "+command[14])

                    

                else:
                    
                    print("The "+maxi+" "+command[3]+" from days "+str(date)+" to "+str(date2)+" was "+str(oldChosen)+" "+res["daily_units"][dataPoint]+" which is "+lessThan+ " "+str(chosen)+" "+res["daily_units"][dataPoint]+" at latitude "+command[11]+" longitude "+command[14])

                

        elif len(command) == 11:
            latitude = "latitude="+command[7]
            longitude = "longitude="+command[10]
            url = url.replace('latitude=52.52',(latitude))
            url = url.replace('longitude=13.41',(longitude))
            startDate = "start_date="+command[4]
            endDate = "end_date="+command[4]
            url = url.replace("start_date=2024-04-11",startDate)
            url = url.replace("end_date=2024-08-11",endDate)
            
            dataPoint = command[2]
            if dataPoint == "weather_code":
                dataPoint = "weather_code"
            elif dataPoint == "temperature_max":
                dataPoint = "temperature_2m_max"
            elif dataPoint == "temperature_min":
                dataPoint = "temperature_2m_min"
            elif dataPoint == "precipitation_sum":
                dataPoint = "precipitation_sum"
            elif dataPoint == "wind_speed_max":
                dataPoint= "wind_speed_10m_max"
            elif dataPoint == "precipitation_probability_max":
                dataPoint = "precipitation_probability_max"
            url = url.replace("weather_code",dataPoint)
            response = requests.get(url)
            data = response.text
            res = json.loads(data)

            place = (index["date"]).index(command[4])

            if dataPoint == "precipitation_probability_max":
                print("In the given data the "+str(command[2])+" was "+str((index[command[2]])[place])+"%"+" while at latitude "+str(command[7])+" and longitude "+str(command[10])+" it was "+(str(res["daily"][dataPoint][0])+"%"))

            else:
                
                print("In the given data the "+str(command[2])+" was "+str((index[command[2]])[place])+" "+res["daily_units"][dataPoint]+" while at latitude "+str(command[7])+" and longitude "+str(command[10])+" it was "+(str(res["daily"][dataPoint][0])+" "+res["daily_units"][dataPoint]))
        elif len(command) == 14:
            latitude = "latitude="+command[10]
            longitude = "longitude="+command[13]
            url = url.replace('latitude=52.52',(latitude))
            url = url.replace('longitude=13.41',(longitude))
            startDate = "start_date="+command[5]
            endDate = "end_date="+command[7]
            url = url.replace("start_date=2024-04-11",startDate)
            url = url.replace("end_date=2024-08-11",endDate)
            maxi = command[2].lower()
            dataPoint = command[3]
            if dataPoint == "weather_code":
                dataPoint = "weather_code"
            elif dataPoint == "temperature_max":
                dataPoint = "temperature_2m_max" 
            elif dataPoint == "temperature_min":
                dataPoint = "temperature_2m_min"
            elif dataPoint == "precipitation_sum":
                dataPoint = "precipitation_sum"
            elif dataPoint == "wind_speed_max":
                dataPoint= "wind_speed_10m_max"
            elif dataPoint == "precipitation_probability_max":
                dataPoint = "precipitation_probability_max"
            url = url.replace("weather_code",dataPoint)
            response = requests.get(url)
            data = response.text
            res = json.loads(data)
            placeStart = (index["date"]).index(command[5])
            placeEnd = (index["date"]).index(command[7])
            oldData = (index[command[3]])[placeStart:placeEnd+1]
            if maxi == 'maximum':
                chosen = findMax(res["daily"][dataPoint])
                oldChosen = findMax(oldData)
            elif maxi == 'minimum':
                chosen = findMin(res["daily"][dataPoint])
                oldChosen = findMin(oldData)
            elif maxi == 'average':
                chosen = findAvg(res["daily"][dataPoint])
                oldChosen = findAvg(oldData)

            lessThan = "equal to"
            if float(oldChosen) < chosen:
                lessThan = "less than"
            elif float(oldChosen) > chosen:
                lessThan = "greater than"

                
            if dataPoint == "precipitation_probability_max":
                print("The "+maxi+" "+command[3]+" from "+command[5]+" to "+command[7]+" was "+str(oldChosen)+"%"+" which is "+lessThan+ " "+str(chosen)+"%"+" at latitude "+command[10]+" longitude "+command[13])
            else:
                

                print("The "+maxi+" "+command[3]+" from "+command[5]+" to "+command[7]+" was "+str(oldChosen)+" "+res["daily_units"][dataPoint]+" which is "+lessThan+ " "+str(chosen)+" "+res["daily_units"][dataPoint]+" at latitude "+command[10]+" longitude "+command[13])
            

            

                
            
    else:
        if len(command) == 9:
            vari = command[2]
            dateOne = int(command[5])
            dateTwo = int(command[8])
            data= (index[vari])[dateOne:dateTwo+1]

            if command[0].lower() == "max" or command[0].lower() == "maximum":
                print("The "+command[0].lower()+" of "+vari+" from days "+str(dateOne)+" to "+str(dateTwo)+" is "+str(findMax(data)))

            elif command[0].lower() == "min" or command[0].lower() == "minimum":

                print("The "+command[0].lower()+" of "+vari+" from days "+str(dateOne)+" to "+str(dateTwo)+" is "+str(findMin(data)))


            elif command[0].lower() == "avg" or command[0].lower() == "average" :
                print("The "+command[0].lower()+" of "+vari+" from days "+str(dateOne)+" to "+str(dateTwo)+" is "+str(findAvg(data)))
            else:
                print('Oops! That command is not recognized. Could you try one that starts with "Min", "Max", or "Average"?')
        else:
            vari = command[2]
            dateOne = (command[4])
            dateTwo = command[6]
            place1 = (index["date"]).index(dateOne)
            place2=(index["date"]).index(dateTwo)
            data= (index[vari])[place1:place2+1]
            if command[0].lower() == "max" or command[0].lower() == "maximum":
                print("The "+command[0].lower()+" of "+vari+" from "+str(dateOne)+" to "+str(dateTwo)+" is "+str(findMax(data)))

            elif command[0].lower() == "min" or command[0].lower() == "minimum":

                print("The "+command[0].lower()+" of "+vari+" from "+str(dateOne)+" to "+str(dateTwo)+" is "+str(findMin(data)))


            elif command[0].lower() == "avg" or command[0].lower() == "average" :
                print("The "+command[0].lower()+" of "+vari+" from "+str(dateOne)+" to "+str(dateTwo)+" is "+str(findAvg(data)))
            else:
                print('Oops! That command is not recognized. Could you try one that starts with "Min", "Max", or "Average"?')
            
            
                                
            
        
    print("")
    
file.close()
