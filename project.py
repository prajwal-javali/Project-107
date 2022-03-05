import plotly.express as px
import pandas as p

df = p.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean() 
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()