import os
from turtle import color, title
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def devNameAndColor(dev):
    dev = os.path.splitext(dev)[0].split("_")[0]
    if(dev == "S1"): return ("dev_16", "#0000ff")
    if(dev == "S2"): return ("dev_18", "#FF0404")
    if(dev == "S5"): return ("dev_17", "#47CF0F")
    return (dev, '#000000')
    

typ = "piłka"
how = "jedna"
dataPath = os.path.join("data", typ)
quaternions = ["Q0", "Q1", "Q2", "Q3"]
people = ["Kost", "Michał", "Rogu"]


fig = make_subplots(rows=4, cols=3, column_titles=people, row_titles=quaternions)
fig.update_layout(title_text="Quaternions - " + typ +" ("+ how +" noga)", showlegend=False)


for i, (p) in enumerate(people):
    filePath = os.path.join(dataPath, p, how)
    if(os.path.isdir(filePath)):
        devices = os.listdir(filePath)
        for dev in devices:
            devName, devColor = devNameAndColor(dev)
            df = pd.read_csv(os.path.join(filePath, dev))
            for qw_i, (qw) in enumerate(quaternions):
                print(qw)
                y = df[qw]
                x = np.arange(len(y))
                fig.add_trace(go.Scatter(x=x, y=y, name=devName, mode='lines', line=dict(color=devColor)), row=qw_i+1, col=i+1)

fig.show() # tylko wyświetla
fig.write_html(os.path.join("qPlots", typ + "-" + how + "_plot.html"), auto_open=False) # zapis do pliku html
