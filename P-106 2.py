import plotly.express as pe
import pandas as pd
import csv

df=pd.read_csv("Marks.csv")
graph=pe.scatter(df,x="Days Present",y="Marks In Percentage")
graph.show()