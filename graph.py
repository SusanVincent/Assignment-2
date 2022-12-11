# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 23:54:31 2022

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_file(fname):
    data = pd.read_excel(fname)
    dtranspose= data.set_index('Country Name').transpose()
    return data, dtranspose
    

coun_list1= ['Austria','Brazil','Colombia','Spain']

coun_list2= ['Estonia','Finland','India','Japan','Mauritius']

def filter_line_data(data):
    data = data[['Country Name','Indicator Name','2010','2011','2012','2013','2014']]
    data = data [(data["Country Name"]=="Austria") | 
                 (data["Country Name"]=="Brazil") | 
                 (data["Country Name"]=="Colombia") |
                 (data["Country Name"]=="Spain")]              
    return data

def filter_bar_plot(data):
    data = data[['Country Name','Indicator Name','2010','2011','2012']]
    data =data [(data["Country Name"]=="Estonia") | 
                (data["Country Name"]=="Finland") | 
                (data["Country Name"]=="India") |
                (data["Country Name"]=="Japan") |
                (data["Country Name"]=="Mauritius")]
    return data
    
    
def barplot(data, label1, label2):
    plt.figure(figsize=(30,20))
    ax= plt.subplot(1,1,1)
    x = np.arange(5)
    width= 0.15

    bar1= ax.bar(x, data["2010"],width, label= 2010)
    bar2= ax.bar(x+width, data["2011"],width, label=2011)
    bar3= ax.bar(x+width*2, data["2012"],width, label=2012)
    
    ax.set_xlabel("Country Names", fontsize= 40)
    ax.set_ylabel(label1, fontsize= 40)
    ax.set_title(label2, fontsize=40)
    ax.set_xticks(x, coun_list2, fontsize=30)
    ax.legend(fontsize=30)
             
    ax.bar_label(bar1, padding=2, rotation=90, fontsize= 20)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize= 20)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize= 20)
    
    plt.show()    
     
           
def line_plot(data,label1,label2):
    plt.figure(figsize=(25,16))
    dd = data.set_index('Country Name')
    tran = dd.transpose()
    tran = tran.drop(index=['Indicator Name'])
    for i in range(len(coun_list1)):
        plt.plot(tran.index, tran[coun_list1[i]], label=coun_list1[i])
        
    plt.title(label2, size=20)
    plt.xlabel("Years", size=16)
    plt.ylabel(label1, size=16)
    plt.xticks(rotation=90)
    plt.legend(fontsize=18)
    plt.savefig("lineplot.png")
    plt.show()
             
Energy_data, Energy_data1 = read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\Enery Use.xls")             
Energy_data= filter_bar_plot(Energy_data) 
Co2_data, Co2_data1=read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\CO2 Emission metric tons per capita.xls")   
Co2_data= filter_bar_plot(Co2_data)
   
power_data, power_data1 = read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\Electric power consumption.xls") 
power_data= filter_line_data(power_data)
Population_data, Population_data1 = read_file("C:\\Users\\user\\Desktop\\asgmnt 2\\Total population.xls")
Population_data = filter_line_data(Population_data)
      

barplot(Energy_data, "Kg of oil equivalent per capita","Energy Consumption")
barplot(Co2_data, 'Metric tons per capita','Co2 Emission') 

line_plot(power_data,"kWh per capita","Electric Power consumption")
line_plot(Population_data,"Range","Total Population")