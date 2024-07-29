from detector import df
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource

df["Start_string"]=df['START'].dt.strftime("%d/%m/%Y %H:%M:%S")
df["End_string"]=df['END'].dt.strftime("%d/%m/%Y %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100,width=500,
         sizing_mode="scale_both",title='MOTION DETECTION GRAPH')
p.title.align="center"
p.title.text_color = "red"

p.yaxis.minor_tick_line_color = None

hover=HoverTool(tooltips=[("Start ","@Start_string"),
                          ("End ","@End_string")])
p.add_tools(hover)
q=p.quad(left='START', right='END', bottom=0, top=1,
         color="green", source=cds)

output_file("Graph.html")
show(p)
