import pandas as pd
import plotly.express as pe

df=pd.read_csv("Coffee .csv")
graph=pe.scatter(df,x="Coffee in ml",y="sleep in hours")
graph.show()