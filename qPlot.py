import os
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go



fig2 = make_subplots(rows=4, cols=1)
fig2.update_layout(title_text="Quaternions")

# ścieżka danych
dataPath = os.path.join("data","1tydz_pilka kostu")
# rodzaje, które były zapisywane
types = ["bez oczu dwie", "bez oczu jedna", "dwie", "jedna"]


for t in types:
    dataFrames = os.listdir(os.path.join(dataPath, t))
    for df in dataFrames:
        print(df)
        V = pd.read_csv(os.path.join(dataPath, t, df))
        print(V.shape)
        v1 = V['Q0']
        v2 = V['Q1']
        v3 = V['Q2']
        v4 = V['Q3']
        # jeśli chcemy poszczególne czujniki, to musimy przesunąć fig2.add_trace o jeden TAB w prawo ;)
    fig2.add_trace(go.Line(x=np.arange(len(v1)), y=v1, name="Q1" + t), row=1, col=1) 
    fig2.add_trace(go.Line(x=np.arange(len(v2)), y=v2, name="Q2" + t), row=2, col=1)
    fig2.add_trace(go.Line(x=np.arange(len(v3)), y=v3, name="Q3" + t), row=3, col=1)
    fig2.add_trace(go.Line(x=np.arange(len(v4)), y=v4, name="Q4" + t), row=4, col=1)

# fig2.add_trace(go.Line(x=np.arange(len(v1)), y=v1, name="Q1"), row=1, col=1)
# fig2.add_trace(go.Line(x=np.arange(len(v2)), y=v2, name="Q2"), row=2, col=1)
# fig2.add_trace(go.Line(x=np.arange(len(v3)), y=v3, name="Q3"), row=3, col=1)
# fig2.add_trace(go.Line(x=np.arange(len(v4)), y=v4, name="Q4"), row=4, col=1)


# fig2.write_html('ECGsygnay.html', auto_open=True) # zapis do pliku html
fig2.show() # tylko wyświetla