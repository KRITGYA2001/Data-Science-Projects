#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import os
from PIL import ImageTk,Image
import numpy as np
import pandas as pd
import seaborn as sns
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[2]:


def Fuel_Price_Prediction():
    def ints():
        try:
            date=int(d.get())
            month=int(m.get())
            year=int(y.get())
            inputs(date,month,year)
        except:
            messagebox.showwarning("Error","Wrong Input")   
    
    def inputs(date,month,year):
        
        data=pd.read_csv("ProjectFile2.csv")
        Date=data[['Date','Month','Year']]
        Petrol=data['Delhi']
        lst=LinearRegression()
        lst.fit(Date,Petrol)
        test=[[date,month,year]]
        predict=lst.predict(test)
        tk.Label(text="The Predicted price of Petrol is:- "+str(round(predict[0],3)),bg="#F8B88B").place(x=100,y=300)
        X_train,X_test,y_train,y_test=train_test_split(Date,Petrol,test_size=0.2)
        clf=LinearRegression()
        clf.fit(X_train,y_train)
        predict=clf.predict(X_test)
        tk.Label(text="The accuracy of the Fuel Prediction is:- "+str(round(clf.score(X_test,y_test),8)),bg="#F8B88B").place(x=100,y=320)
        
    def calling6():
        fppwin.destroy()
        menu_win()
    
    fppwin=tk.Tk()
    fppwin.geometry('500x500')
    fppwin.title("Fuel Price Window")
    fppwin.configure(background="#F8B88B")
    tk.Label(fppwin,text="Fuel Price Prediction",font=("Amiri",14),bg="#F8B88B").pack()
    tk.Label(fppwin,text="Date",bg="#F8B88B").place(x=150,y=110)
    tk.Label(fppwin,text="Month",bg="#F8B88B").place(x=150,y=150)
    tk.Label(fppwin,text="Year",bg="#F8B88B").place(x=150,y=190)
    d=tk.Entry(fppwin)
    m=tk.Entry(fppwin)
    y=tk.Entry(fppwin)
    d.place(x=200,y=111)
    m.place(x=200,y=151)
    y.place(x=200,y=191)
    tk.Button(fppwin,text="Show",command=ints,width=10,activebackground="black",activeforeground="red",bg="yellow").place(x=220,y=230)
    tk.Button(fppwin,text="Mainmenu",command=calling6,width=10,activebackground="cyan",activeforeground="pink",bg="yellow").place(x=110,y=450)
    tk.Button(fppwin,text="Exit",command=fppwin.destroy,width=10,activebackground="cyan",activeforeground="pink",bg="yellow").place(x=310,y=450)
    tk.mainloop()


def fuel_consumed_prediction():
    def ints_t():
        try:
            Distance=int(dis.get())
            horsepower=int(hor.get())
            weight=int(wei.get())
            acceleration=float(acc.get())
            input2(Distance,horsepower,weight,acceleration)
        except:    
            messagebox.showwarning("Showerror","Wrong Input")
    
    def input2(Distance,horsepower,weight,acceleration):
        data=pd.read_csv("ProjectFile3.csv")
        x=data[["Distance","horsepower","weight","acceleration"]]
        y=data["cylinders"]
        lst=LinearRegression()
        lst.fit(x,y)
        test_data=[[Distance,horsepower,weight,acceleration]]
        predict=lst.predict(test_data)
        tk.Label(text="The Cylinders used are:- "+str(round(predict[0],3)),bg="#DA70D6").place(x=100,y=320)
        X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
        regr=LinearRegression()
        regr.fit(X_train,y_train)
        predict=regr.predict(X_test)
        temp=regr.score(X_test,y_test)
        tk.Label(text="The accuracy of Fuel consume on distance is :- "+str(round(temp,8)),bg="#DA70D6").place(x=100,y=340)
     
    def calling7():
        fcpwin.destroy()
        menu_win()
    
    fcpwin=tk.Tk()
    fcpwin.geometry('500x500')
    fcpwin.title("Fuel Consume Window")
    fcpwin.configure(background="#DA70D6")
    tk.Label(fcpwin,text="Fuel Consume Prediction",bg="#DA70D6",font=("Amiri",14)).pack()
    tk.Label(fcpwin,text="Distance(km)",bg="#DA70D6").place(x=115,y=110)
    tk.Label(fcpwin,text="HorsePower(hp)",bg="#DA70D6").place(x=115,y=150)
    tk.Label(fcpwin,text="Weight(kg)",bg="#DA70D6").place(x=115,y=190)
    tk.Label(fcpwin,text="Acceleration(m/s)",bg="#DA70D6").place(x=115,y=230)
    dis=tk.Entry(fcpwin)
    hor=tk.Entry(fcpwin)
    wei=tk.Entry(fcpwin)
    acc=tk.Entry(fcpwin)
    dis.place(x=220,y=112)
    hor.place(x=220,y=152)
    wei.place(x=220,y=192)
    acc.place(x=220,y=232)
    tk.Button(fcpwin,text="Show",command=ints_t,width=10,activebackground="black",activeforeground="red",bg="yellow").place(x=240,y=265)
    tk.Button(fcpwin,text="Mainmenu",command=calling7,width=10,activebackground="cyan",activeforeground="pink",bg="yellow").place(x=110,y=450)
    tk.Button(fcpwin,text="Exit",command=fcpwin.destroy,width=10,activebackground="cyan",activeforeground="pink",bg="yellow").place(x=310,y=450)
    tk.mainloop()   
    
    

def car_selling_prediction():
    def ints3():
        try:
            Distance=int(dis.get())
            horsepower=float(hor.get())
            weight=int(wei.get())
            acceleration=int(acc.get())
            input3(Distance,horsepower,weight,acceleration)
        except:
            messagebox.showerror("ShowError","Wrong Input")
            
    
    def input3(Distance,horsepower,weight,acceleration):
        data=pd.read_csv("ProjectFile1.csv")
        x=data[['Year','Present_Price','Kms_Driven','Fuel_Type']]
        y=data['Selling_Price']
        lst=LinearRegression()
        lst.fit(x,y)
        test_data=[[Distance,horsepower,weight,acceleration]]
        predict=lst.predict(test_data)
        os.system('cls')
        time.sleep(0.25)
        tk.Label(text="The Selling Price of Your Car is:- "+str(round(predict[0],3)),bg="#E2F516").place(x=100,y=350)
        X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.4)
        regr=LinearRegression()
        regr.fit(X_train,y_train)
        predict=regr.predict(X_test)
        temp=regr.score(X_test,y_test)
        tk.Label(text="The accuracy of the Car selling price is:- "+str(round(temp,8)),bg="#E2F516").place(x=100,y=370)
     
    def calling8():
        cspwin.destroy()
        menu_win()
    
    cspwin=tk.Tk()
    cspwin.geometry('500x500')
    cspwin.title("Fuel Consume Window")
    cspwin.configure(background="#E2F516")
    tk.Label(cspwin,text="Car Selling Price Prediction",bg="#E2F516",font=("Amiri",14)).pack()
    tk.Label(cspwin,text="Car Purchase Year:- ",bg="#E2F516").place(x=110,y=110)
    tk.Label(cspwin,text="Present Showroom Price of Your Car's Model(Lakh):- ",bg="#E2F516").place(x=110,y=150)
    tk.Label(cspwin,text="Kilometers Driven:- ",bg="#E2F516").place(x=110,y=205)
    tk.Label(cspwin,text="Fuel Type('Petrol:0','Diesel:1','CNG:2'):- ",bg="#E2F516").place(x=110,y=245)
    dis=tk.Entry(cspwin)
    hor=tk.Entry(cspwin)
    wei=tk.Entry(cspwin)
    acc=tk.Entry(cspwin)
    dis.place(x=220,y=112)
    hor.place(x=220,y=172)
    wei.place(x=220,y=207)
    acc.place(x=220,y=266)
    tk.Button(cspwin,text="Show",command=ints3,width=10,activebackground="black",activeforeground="green",bg="#D891EF").place(x=240,y=305)
    tk.Button(cspwin,text="Mainmenu",command=calling8,width=10,activebackground="cyan",activeforeground="pink",bg="#D891EF").place(x=110,y=450)
    tk.Button(cspwin,text="Exit",command=cspwin.destroy,width=10,activebackground="cyan",activeforeground="pink",bg="#D891EF").place(x=310,y=450)
    tk.mainloop()          


# In[3]:


def Distance_consume_Dataset():
    data=pd.read_csv("ProjectFile3.csv")
    print("All Data Graph")
    sns.pairplot(data,palette="brg")
    plt.show()
    print("\n\n\n")
    sns.set_style("whitegrid",{'axes.edgecolor': 'red'})
    sns.relplot(x="cylinders",y="horsepower",data=data).set(title='Cylinders vs horsepower')
    plt.show()
    print("\n\n\n")
    sns.set_style("whitegrid",{'axes.edgecolor': 'red'})
    sns.relplot(x="horsepower",y="acceleration",data=data).set(title='Horsepower vs acceleration')
    plt.show()
    print("\n\n\n")
    plt.title("Cylinders Vs horsepower")
    sns.stripplot(x="cylinders",y="horsepower",data=data,jitter=True)
    plt.show()
    print("\n\n\n")
    plt.title("Cylinders vs acceleration")
    sns.stripplot(x="cylinders",y="acceleration",data=data,jitter=False)
    plt.show()
    print("\n\n\n")
    plt.title("Cylinders vs acceleration")
    sns.boxplot(x="cylinders",y="acceleration",data=data)
    plt.show()   
    
    
def fuel_price_Dataset():
    data=pd.read_csv("ProjectFile2.csv")
    print("All Data Graph")
    sns.pairplot(data,palette="brg")
    plt.show()
    print("\n\n\n")
    sns.set_style("darkgrid",{'axes.edgecolor': 'red'})
    sns.relplot(x="Year",y="Delhi",data=data)
    plt.title("Year vs Petrol Price")
    plt.show()
    print("\n\n\n")
    print("Petrol Prices graph")
    plt.title("Year vs Petrol Price")
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
    
    
def Car_Price_Dataset():
    print("All Data Graph")
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


# In[4]:


def Graph_representation_of_dataset():
    def des():
        grod.destroy()
        menu_win()
    global grod
    grod=tk.Tk()
    grod.geometry('400x400')
    grod.title("Datasets")
    grod.configure(background="#00BFFF")
    tk.Label(text="Dataset Menu",font=("Amiri",16),bg="#00BFFF").pack()
    tk.Button(text="Fuel Price Prediction Dataset",command=fuel_price_Dataset,bg="yellow").place(x=120,y=120)
    tk.Button(text="Fuel Consumed Prediction Dataset",command=Distance_consume_Dataset,bg="yellow").place(x=103,y=160)
    tk.Button(text="Car Selling Price Prediction Dataset",command=Car_Price_Dataset,bg="yellow").place(x=103,y=200)
    tk.Button(text="Mainmenu",command=des,width=9,bg="yellow").place(x=160,y=240)
    tk.Button(text="Exit",command=grod.destroy,width=9,bg="yellow").place(x=160,y=280)
    tk.mainloop()


def menu_win():
    def calling2():
        menuwin.destroy()
        Fuel_Price_Prediction()
        
    def calling3():
        menuwin.destroy()
        fuel_consumed_prediction()
        
    def calling4():
        menuwin.destroy()
        car_selling_prediction()
        
    def calling5():
        menuwin.destroy()
        Graph_representation_of_dataset()
    
    global menuwin
    menuwin=tk.Tk()
    menuwin.geometry('500x500')
    menuwin.title("Menu")
    menuwin.configure(background='#856ff8')
    tk.Label(menuwin,text="Hello",fg='black',bg='#856ff8',font=("Amiri",15)).place(x=230,y=0)
    tk.Label(menuwin,text=" Welcome to the Fuel Prediction Project",bg='#856ff8').place(x=140,y=65)
    tk.Button(menuwin,text="       1:  Fuel Price Prediction        ",bg='yellow',fg='black',command=calling2).place(x=160,y=130)
    tk.Button(menuwin,text="       2:  Fuel Consumed Prediction        ",bg='yellow',fg='black',command=calling3).place(x=144,y=175)
    tk.Button(menuwin,text="       3:  Car Selling Price Prediction        ",bg='yellow',fg='black',command=calling4).place(x=144,y=220)
    tk.Button(menuwin,text="       4:  Graph Reprentation of Datasets        ",bg='yellow',fg='black',command=calling5).place(x=135,y=265)
    tk.Button(menuwin,text="       5:  Exit        ",bg='yellow',fg='black',command=menuwin.destroy).place(x=205,y=310)
    tk.mainloop()


# In[7]:






def main():
    def calling1():
        master.destroy()
        menu_win()
    global master
    master=tk.Tk()
    master.geometry('320x210')
    master.title("Main Window")
    img=PhotoImage(file='main.png')
    tk.Label(master,image=img).pack()
    tk.Label(master,text="Main Window",bg='#0096FF').place(x=120,y=45)
    tk.Button(master,text="  Menu  ",fg='cyan',bg='black',command=calling1).place(x=90,y=140)
    tk.Button(master,text="    Exit    ",fg='cyan',bg='black',command=master.destroy).place(x=170,y=140)
    tk.mainloop()


main()


# In[ ]:




