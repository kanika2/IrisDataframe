import tkinter as tk
from tkinter import Tk, Button, Label, Entry,Menubutton,Menu
import mysql.connector as cc
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

#dataframe of url
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv(url, names=names)
#df=pd.DataFrame(dataset)

#sql command
con =cc.connect(host='localhost',database='iris',user='root',password='root')
cur=con.cursor()
#cur.execute("drop table pd")
#print('Table is dropped')
'''
cur.execute("drop table iris_data")
print('Table is dropped')
'''
try:
    sql = 'Create table iris_data(sepal_length float not null,sepal_width float not null,petal_length float not null,petal_width float not null,class varchar(30) not null)'
    cur.execute(sql)
    print('table created succesfully!')
    sl=[]
    sw=[]
    pl=[]
    pw=[]
    cl=[]
    #data in list
    for i in df['sepal-length']:
        sl.append(i)
    for i in df['sepal-width']:
        sw.append(i)
    for i in df['petal-length']:
        pl.append(i)
    for i in df['petal-width']:
        pw.append(i)
    for i in df['class']:
        cl.append(i)

    for r in range(0,len(sl)):
        #cur.execute('insert into pd values(%s,%s)',(1,2))
        cur.execute('insert into iris_data values(%s,%s,%s,%s,%s)',(sl[r],sw[r],pl[r],pw[r],cl[r]))
    print('Data is entered')
except:
    print('Table already created')

#creating database data into dataframe
cur.execute('select * from iris_data')
result=cur.fetchall()
d=pd.DataFrame(data=result,columns=['sepal-length','sepal-width','petal-length','petal-width','class'])
print(d)

con.commit()
cur.close()
con.close()

#gui interface
def desc():
    ch = txt1.get()
    c=str(d.describe()[ch])
    out1.configure(text=c)

def graph():
    ch = txt2.get()
    grp=d.groupby(ch).size()
    grp.plot(kind='bar', subplots=True, layout=(2,2),sharex=False,sharey=False)
    plt.show()   #display the graph in new window

def col():
    ch=txt3.get()
    c=str(d[ch])
    out3.configure(text=c)

root=Tk()
root.title('My first gui')  #title of the window
root.geometry('800x1000') 

lb1 = Label(text='Enter the column to describe')
lb1.grid(column=0,row=1)
txt1 = Entry()
txt1.grid(column=1,row=1)
data1 = Button(text='Show Describe:',command= desc)
data1.grid(column=4,row=1)
out1=Label()
out1.grid(column=0,row=2)

lb2 = Label(text='Enter the column to draw graph of')
lb2.grid(column=0,row=3)
txt2 = Entry()
txt2.grid(column=1,row=3)
data2 = Button(text='Show Graph:',command= graph)
data2.grid(column=4,row=3)

lb3 = Label(text='Enter the column to see')
lb3.grid(column=0,row=4)
txt3 = Entry()
txt3.grid(column=1,row=4)
data3 = Button(text='Show Column:',command= col)
data3.grid(column=4,row=4)
out3=Label()
out3.grid(column=0,row=5)

bt = Button(text='close',command = exit)
bt.grid(column=2, row=0)

root.mainloop()