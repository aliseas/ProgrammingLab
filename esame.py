#Importing needed/useful modules
import os 
import numpy as np

#CLASS FOR EXCEPTIONS
class ExamException(Exception):
    pass

#CLASS FOR FILE TO READ
class CSVTimeSeriesFile():
    #ATTRIBUTES
    def __init__(self,name):
        self.name = name
    #METHODS
    def get_data(self):
        file_list = []
        #checking if file exists/is accessible
        if not os.path.isfile(self.name):
            raise ExamException("Cannot find file:'{}'. File not on path".format(self.name))
        file = open(self.name)
        #checking if file is readable
        if not os.access(self.name, os.R_OK):
            raise ExamException("Error: File '{}' is not readable.'".format(self.name))
        #checking if file is not empty
        filesize = os.path.getsize(self.name)
        if filesize == 0:
            raise ExamException("Encountered problem: The file is empty")
        lines = file.readlines()
        line_number = 0
        for line in lines:
            line_number += 1
            line = line.strip()
            line = line.split(',')
            #checking if empty line or incorrect number of elements (and ignoring line)
            if(len(line)!=2 ):
                continue
            if 'prev_timestamp' not in locals():
                prev_timestamp = 0;
            #Checking timestamps
            #checking for non-digit timestamps (and ignoring line)
            line[0] = line[0].strip()
            check_line = line[0]
            check_line = check_line.replace(".","")
            if not(check_line.isdigit()):
                continue
            #checking for none/empty timestamps (and ignoring line)
            if(line[0]=='None' or line[0]=='' or len(line[0])==0):
                continue
            line[0] = int(float(line[0])) #converting first to float to avoid problems in converting possible string floats into integers
            #exception for order of timestamps
            if(line_number!=1 and line[0]<prev_timestamp):
                raise ExamException("Problem: Timestamps in incorrect order.")
            #exception for duplicate timestamps 
            if(line_number!=1 and prev_timestamp==line[0]): 
                raise ExamException("Problem: Duplicated timestamps.")
            #checking for negative timestamps (and ignoring line)
            if(line[0]<=0):
                continue
            #Checking temperature values
            #checking for none/empty values for temperature
            line[1] = line[1].strip()
            if(line[1]=='None' or line[1]=='' or len(line[1])==0):
                continue
            #checking for non-numeric value in temperature value
            temp_line = line[1] #using a variable to not fiddle with line[1]
            temp_line = temp_line.replace(".", "") #floating point numbers must still be numbers for isdigit
            temp_line = temp_line.replace("-", "") #negative numbers must still be numbers for isdigit
            if(temp_line.isdigit()):
                line[1] = float(line[1])
            else:
                continue
            file_list.append(line) 
            prev_timestamp = line[0]
        file.close()
        return(file_list)

#FUNCTION TO COMPUTE DAILY STATISTICS REGARDING THE FILE MANAGED BY THE CLASS
def daily_stats(input_list):
    output_list = []
    list_length = len(input_list)#helps to check when I get to the last list
    count = 0
    for el_list in input_list:
        count += 1
        epoch = el_list[0]
        day_start_epoch = epoch - (epoch % 86400)
        if 'prev_start_epoch' not in locals():
            prev_start_epoch = day_start_epoch
            temp_list = []
            stat_list = []
        if(day_start_epoch != prev_start_epoch):
            #compute min,max,mean temp of prev timestamps
            stat_list.append(min(temp_list))
            stat_list.append(max(temp_list))
            stat_list.append(np.mean(temp_list))
            output_list.append(stat_list)
            stat_list = []
            temp_list = []
            if(count==list_length):
                temp_list.append(el_list[1])
                stat_list.append(min(temp_list))
                stat_list.append(max(temp_list))
                stat_list.append(np.mean(temp_list))
                output_list.append(stat_list)
            else:
                prev_start_epoch = day_start_epoch
                temp_list.append(el_list[1])
        else:
            if(count==list_length):
                temp_list.append(el_list[1])
                stat_list.append(min(temp_list))
                stat_list.append(max(temp_list))
                stat_list.append(np.mean(temp_list))
                output_list.append(stat_list)
            else:
                temp_list.append(el_list[1])
    return(output_list)

#IMPLEMENTING CLASS
time_series_file = CSVTimeSeriesFile(name='data.csv')
#time_series_file = CSVTimeSeriesFile(name='pr.pr') #empty test file
#time_series_file = CSVTimeSeriesFile(name='inesistente.csv') #test file
#time_series_file = CSVTimeSeriesFile(name='file.csv') #test file
time_series = time_series_file.get_data()
print(time_series)

#IMPLEMENTING FUNCTION
stats_list = daily_stats(time_series)
print(stats_list)
