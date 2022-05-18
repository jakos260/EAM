import os
from turtle import color, st, title
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from scipy.fft import fft, fftfreq


N = 1000

def fftProcess(y):
    T = 1.0/100.0
    n_2 = int(N/2)

    yf = np.fft.fft(np.array(y))
    yf = 2.0/N * np.abs(yf[:n_2])
    xf = np.fft.fftfreq(N, T)[:n_2]

    return (xf, yf)

def devNameAndColor(dev):
    dev = os.path.splitext(dev)[0].split("_")[0]
    if(dev == "S1"): return (devName[0], "#0000ff")
    if(dev == "S2"): return (devName[2], "#FF0404")
    if(dev == "S5"): return (devName[1], "#47CF0F")
    return (dev, '#000000')

def pNameAndColor(p):
    if(p == people[0]): return (people[0], "#0000ff")
    if(p == people[1]): return (people[1], "#FF0404")
    if(p == people[2]): return (people[2], "#47CF0F")
    return (p, '#000000')
    

typ = "piłka"
howManyLegs = ["jedna", "dwie", "bez oczu jedna", "bez oczu dwie"]
how = howManyLegs[0]
dataPath = os.path.join("data", typ)
quaternions = ["Q0", "Q1", "Q2", "Q3"]
gyro = ["GyrX","GyrY","GyrZ"]
people = ["Kost", "Michał", "Rogu"]
# devName = ["dev_16", "dev_17", "dev_18"]
devName = ["kostka", "nadgarstek", "biodro"]
title = "Gyroscope - " + typ +" ("+ how +" noga)"

fig = make_subplots(rows=3, cols=3, column_titles=devName, row_titles=gyro)
fig.update_layout(title_text=title, showlegend=False)


for i, (p) in enumerate(people):
    filePath = os.path.join(dataPath, p, how)
    if(os.path.isdir(filePath)):
        devices = os.listdir(filePath)
        for dev_i, (dev) in enumerate(devices):
            devName, devColor = pNameAndColor(p)
            df = pd.read_csv(os.path.join(filePath, dev))
            for qw_i, (qw) in enumerate(gyro):
                print(qw)
                y = df[qw]*250/32768
                # start = 1000 # 3:1000; 2:0; 1:500; 0:200
                # y = y[start:start+N]
                # x = np.arange(0, len(y)/100, 0.01)
                xf, yf = fftProcess(y)

                fig.add_trace(go.Scatter(x=xf, y=yf, name=p, mode='lines', line=dict(color=devColor)), row=qw_i+1, col=dev_i+1)
                fig.update_xaxes(title_text="frequency [Hz]", row=qw_i+1, col=dev_i+1)
                # fig.update_xaxes(title_text="time [s]", row=qw_i+1, col=dev_i+1)
                fig.update_yaxes(title_text="amplitude [°/s]", row=qw_i+1, col=dev_i+1)

fig.show() # tylko wyświetla
fig.write_html(os.path.join("gyroPlots", title + "_plot.html"), auto_open=False) # zapis do pliku html