#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[5]:


def mainmenu():
    os.system('cls')
    print("               Hello                 ")
    print("Welcome to the Fuel Prediction Project")
    time.sleep(0.75)
    print('*'*30)
    print("1:Fuel Price Prediction")
    print("2:Fuel Consumed Prediction")
    print("3:Car Selling Price Prediction")
    print("4:Graph Reprentation of Datasets")
    print("5:Exit")
    print('*'*30)
  
def Price_inputs():
    try:
        d=int(input("Enter the date:- "))
        m=int(input("Enter the month:- "))
        y=int(input("Enter the year:- "))
    except:
        os.system('cls')
        print("Enter integer Value::")
        os.system('cls')
        d,m,y=Price_inputs()
    return d,m,y 


def Fuel_consumed_inputs():
    try:
        Distance=int(input("Distance covered (km/L):- "))
        horsepower=int(input("Horsepower of car:- "))
        weight=int(input("Weight of the car:- "))
        acceleration=float(input("Acceleration from 0 to 60 mph(sec.):- "))
    except:
        os.system('cls')
        print("Enter the required values::")
        os.system('cls')
        Distance,horsepower,weight,acceleration=Fuel_consumed_inputs()
    return  Distance,horsepower,weight,acceleration 


def selling_price_inputs():
    try:
        year=int(input("Car Purchase Year:- "))
        pp=float(input("Present Showroom Price of Your Car's Model(Lakh):- "))
        kd=int(input("Kilometers Driven:- "))
        ft=int(input("Fuel Type('Petrol:0','Diesel:1','CNG:2'):- "))
    except:
        os.system('cls')
        print("Enter the required values::")
        os.system('cls')
        year,pp,kd,ft=selling_price_inputs()
    return year,pp,kd,ft    


def Price_prediction_of_fuel():
    data=pd.read_csv("ProjectFile2.csv")
    os.system('cls')
    Date=data[['Date','Month','Year']]
    Petrol=data["Delhi"]
    lst=LinearRegression()
    lst.fit(Date,Petrol)
    time.sleep(0.25)
    d,m,y=Price_inputs()
    test=[[d,m,y]]
    predict=lst.predict(test)
    os.system('cls')
    print("The Predicted price of Petrol is :- ",round(predict[0],4))
    x=data[['Date','Month','Year']]
    y=data["Delhi"]
    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    clf=LinearRegression()
    clf.fit(X_train,y_train)
    predict=clf.predict(X_test)
    print("The accuracy of the Fuel Prediction is:- ",round(clf.score(X_test,y_test),8))


def fuel_consumed_prediction():
    data=pd.read_csv("ProjectFile3.csv")
    x=data[["Distance","horsepower","weight","acceleration",]]
    y=data["cylinders"]
    lst=LinearRegression()
    lst.fit(x,y)
    os.system('cls')
    time.sleep(0.25)
    Distance,horsepower,weight,acceleration=Fuel_consumed_inputs()
    test_data=[[Distance,horsepower,weight,acceleration]]
    predict=lst.predict(test_data)
    os.system('cls')
    time.sleep(0.25)
    print("The Cylinders used are:- ",round(predict[0]),4)
    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.4)
    regr=LinearRegression()
    regr.fit(X_train,y_train)
    predict=regr.predict(X_test)
    print("The accuracy of Fuel consume on distance is :- ",round(regr.score(X_test,y_test),8))    
    
    
def Car_selling_price():
    data=pd.read_csv("ProjectFile1.csv")
    x=data[['Year','Present_Price','Kms_Driven','Fuel_Type']]
    y=data['Selling_Price']
    lst=LinearRegression()
    lst.fit(x,y)
    os.system('cls')
    time.sleep(0.25)   
    print("Enter Few Details:- ")
    year,pp,kd,ft=selling_price_inputs()
    test_data=[[year,pp,kd,ft]]
    predict=lst.predict(test_data)
    os.system('cls')
    time.sleep(0.25)
    print("The Selling Price of Your Car is:- ",round(predict[0],4)," Lakh")
    train=data[['Year','Present_Price','Kms_Driven','Fuel_Type']]
    test=data['Selling_Price']
    X_train,X_test,y_train,y_test=train_test_split(train,test,test_size=0.4)
    regr=LinearRegression()
    regr.fit(X_train,y_train)
    predict=regr.predict(X_test)
    print("The accuracy of the Car selling price is:- ",round(regr.score(X_test,y_test),8))

    
def Car_Price_Dataset():
    os.system('cls')
    time.sleep(0.25)
    data=pd.read_csv("ProjectFile1.csv")
    sns.set_style("darkgrid",{'axes.edgecolor': 'red','grid.linestyle': ':'})
    sns.pairplot(data)
    plt.show()

    sns.set_style("darkgrid",{'axes.edgecolor': 'green'})
    sns.relplot(x="Year",y="Present_Price",data=data,hue="Fuel_Type",palette="brg")
    plt.title("Year vs Present Price")
    plt.show()

    sns.set_style("darkgrid",{'axes.edgecolor': 'green'})
    sns.jointplot(x="Year",y="Present_Price",data=data,hue="Fuel_Type",palette="brg")
    plt.show()

    sns.swarmplot(x="Fuel_Type",y="Selling_Price",data=data)
    plt.title("Fuel_Type vs Selling_Price")
    plt.show()

    plt.subplot(1,2,1)
    sns.distplot(data['Selling_Price'])
    plt.subplot(1,2,2)
    sns.distplot(data['Year'])
    plt.show()   
    
    
def fuel_price_dataset():
    os.system('cls')
    time.sleep(0.25)
    data=pd.read_csv("ProjectFile2.csv")
    print("All Data Relation in the Dataset")
    sns.pairplot(data,palette="brg")
    plt.show()
    print("\n\n\n")
    sns.set_style("darkgrid",{'axes.edgecolor': 'red'})
    sns.relplot(x="Year",y="Delhi",data=data)
    plt.title("Year vs Petrol Price")
    plt.show()
    print("\n\n\n")
    print("Petrol Prices graph")
    sns.set_style("whitegrid",{'axes.edgecolor': 'green'})
    sns.distplot(data["Delhi"])
    plt.show()
    print("\n\n\n")
    plt.title("Year vs Petrol Price")
    sns.stripplot(x="Year",y="Delhi",data=data,jitter=True)
    plt.show()
    print("\n\n\n")
    plt.title("Month Vs Petrol Price")
    sns.boxplot(x="Month",y="Delhi",data=data)
    plt.show()
    plt.title("Year Vs Petrol Price")
    sns.violinplot(x="Year",y="Delhi",data=data,hue="Month")
    plt.show() 
    
    
def Distance_consume_prediction():
    os.system('cls')
    time.sleep(0.25)
    data=pd.read_csv("ProjectFile3.csv")
    print("All Data Relation in the Dataset")
    sns.pairplot(data,palette="brg")
    plt.show()
    print("\n\n\n")
    sns.set_style("whitegrid",{'axes.edgecolor': 'red'})
    sns.despine()
    sns.relplot(x="cylinders",y="horsepower",data=data)
    plt.title("Cylinders vs horsepower")
    plt.show()
    print("\n\n\n")
    sns.set_style("whitegrid",{'axes.edgecolor': 'red'})
    sns.despine()
    sns.relplot(x="horsepower",y="acceleration",data=data)
    plt.title("Horsepower vs acceleration")
    plt.show()
    print("\n\n\n")
    plt.title("Cylinders Vs horsepower")
    sns.stripplot(x="cylinders",y="horsepower",data=data,jitter=True)
    plt.show()
    print("\n\n\n")
    plt.title("Cylinders vs acceleration")
    sns.stripplot(x="cylinders",y="acceleration",data=data,jitter=True)
    plt.show()
    print("\n\n\n")
    plt.title("Cylinders vs acceleration")
    sns.boxplot(x="cylinders",y="acceleration",data=data)
    plt.show()    
    
    
def Graph_representation_of_dataset():
    found=0
    os.system('cls')
    time.sleep(0.25)
    print("*"*30)
    print("1:Fuel Price Prediction Dataset")
    print("2:Fuel Consumed Prediction Dataset")
    print("3:Car Selling Price Prediction Dataset")
    print("4:Mainmenu")
    print("5:Exit")
    print("*"*30)
    choice=input("Enter Your Choice: ")
    if choice=='1':
        fuel_price_dataset()
    elif choice=='2':
        Distance_consume_prediction()
    elif choice=='3':
        Car_Price_Dataset()
    elif choice=='4':
        main()
        found=1
    elif choice=='5':
        print("Thanku for Choosing Program")
        print("See you soon")
        return
    else:
        os.system('cls')
        print("Wrong Input!!") 
    if found==0:
        time.sleep(0.25)
        Graph_representation_of_dataset()
    
    
def main():
    while True:
        found,a=0,0
        os.system('cls')
        time.sleep(0.2)
        mainmenu()
        print("Please Choose one option:- ")
        choice=input("Enter Your Choice: ")
        if choice=='1':
            Price_prediction_of_fuel()
        elif choice=='2':
            fuel_consumed_prediction()
        elif choice=='3':
            Car_selling_price()
        elif choice=='4':
            Graph_representation_of_dataset()
            found=1
        elif choice=='5':
            os.system('cls')
            time.sleep(0.25)
            print("Thanku for Choosing Program")
            print("See you soon")
            break
        else:
            print("Invalid Input!!")
            continue
        if found==1:
            break
        ch=input("More Operations Y|N: ")
        if ch in 'Nn':
            os.system('cls')
            time.sleep(0.2)
            print("Thanku for Choosing Program")
            print("See you soon")
            break
        
main()        


# In[ ]:




