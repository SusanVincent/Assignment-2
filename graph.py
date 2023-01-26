# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 23:54:31 2022

@author: user
"""
#importing pandas,numpy and matplotlib library files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''Function 'read_file' reads the datasets to the dataframe named data and 
sets the columnn 'Country Name' as index and applies transpose to te data'''
def read_file(fname):
    data = pd.read_excel(fname)
    dtranspose= data.set_index('Country Name').transpose()
    return data, dtranspose

#Choosing countries for plotting the graphs and storing it to the variable, 'count_name' 
count_name= ['Estonia','Finland','India','Japan','Mauritius']

def filter_line_data(data):
    
   data = data[['Country Name','Indicator Name','1990','1995','2000','2005','2010']]
   data =data [(data["Country Name"]=="Estonia") | 
               (data["Country Name"]=="Finland") | 
               (data["Country Name"]=="India") |
               (data["Country Name"]=="Japan") |
               (data["Country Name"]=="Mauritius")]           
   return data

def filter_bar_plot(data):
    
    data = data[['Country Name','Indicator Name','1990','1995','2000','2005','2010']]
    data =data [(data["Country Name"]=="Estonia") | 
                (data["Country Name"]=="Finland") | 
                (data["Country Name"]=="India") |
                (data["Country Name"]=="Japan") |
                (data["Country Name"]=="Mauritius")]
    return data
    
    
def barplot(data, label1, label2):
    """This function plots an bar graph"""
    
    plt.figure(figsize=(30,20))
    
    
    ax= plt.subplot(1,1,1)
    x = np.arange(5)
    width= 0.15

    bar1= ax.bar(x, data["1990"],width, label= 1990)
    bar2= ax.bar(x+width, data["1995"],width, label=1995)
    bar3= ax.bar(x+width*2, data["2000"],width, label=2000)
    bar4= ax.bar(x+width*3, data["2005"],width, label=2005)
    bar5= ax.bar(x+width*4, data["2010"],width, label=2010)
    
    ax.set_xlabel("Country Names", fontsize= 40, c = 'black')
    ax.set_ylabel(label1, fontsize= 40, c = 'black')
    ax.set_title(label2, fontsize=40)
    ax.set_xticks(x, count_name, fontsize=34)
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    ax.legend(fontsize=30)
             
    ax.bar_label(bar1, padding=2, rotation=90, fontsize= 20)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize= 20)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize= 20)
    ax.bar_label(bar4, padding=2, rotation=90, fontsize = 20)
    ax.bar_label(bar5, padding=2, rotation=90, fontsize = 20)
    
    plt.show()    
     
           
def line_plot(data,label1,label2):
    """This function plots the line graph"""
    
    plt.figure(figsize=(25,12))
    dd = data.set_index('Country Name')
    tran = dd.transpose()
    tran = tran.drop(index=['Indicator Name'])
    for i in range(len(count_name)):
        plt.plot(tran.index, tran[count_name[i]], label=count_name[i])
        
    plt.title(label2, size=30)
    plt.xlabel("Years", size=26, c = 'black')
    plt.ylabel(label1, size=26, c = 'black')
    plt.xticks(rotation=90, size=22)
    plt.legend(fontsize=20)
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    plt.show()
    
 
def Co2_data_mean():
        data1,data2 = read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\CO2 Emission metric tons per capita.xls")
        df = data1.set_index("Country Name")
        transpose = df.transpose()
        transpose = df.transpose()
        transpose = transpose.drop(index='Indicator Name')
        transpose = transpose.drop(index='Country Code')
        transpose = transpose.drop(index='Indicator Code')
        cleaned_data = transpose.fillna(0)
        mean = cleaned_data[['Estonia','Finland','India','Japan','Mauritius']].mean()
            
        return mean
    
#Defining the paths of the datasets   
    
Energy_data, Energy_data1 = read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\Enery Use.xls")             
Energy_data= filter_bar_plot(Energy_data) 
Co2_data, Co2_data1=read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\CO2 Emission metric tons per capita.xls")   
Co2_data= filter_bar_plot(Co2_data)
   
power_data, power_data1 = read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\Electric power consumption.xls") 
power_data= filter_line_data(power_data)
Population_data, Population_data1 = read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\Total population.xls")
Population_data = filter_line_data(Population_data)
      
#Labeling the x and y axis of the graphs
barplot(Energy_data, "Kg of oil equivalent per capita","Energy Consumption")
barplot(Co2_data, 'Metric tons per capita','Co2 Emission') 

line_plot(power_data,"kWh per capita","Electric Power consumption" )
line_plot(Population_data,"Population total","Total Population")

#function to return the mean of co2 gas emission
mean = Co2_data_mean()
mean = mean.to_csv("mean_Co2 emission.csv")