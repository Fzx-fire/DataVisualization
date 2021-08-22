from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die1 = Die()
die2=Die()
results = []

for roll_num in range(10000):
    result = die1.roll()+die2.roll()
    results.append(result)

frequencies=[]

max_result=die1.num_sides+die2.num_sides
for i in range(2,max_result+1):
    frequencey=results.count(i)
    frequencies.append(frequencey)


x_values=list(range(2,max_result+1))
# 条形图
data=[Bar(x=x_values,y=frequencies)]
# 标签                         x轴刻度
x_axis_config={'title':'结果','dtick':1}
y_axis_config={'title':'结果的频率'}

my_layout=Layout(title='投掷1000次结果',xaxis=x_axis_config,yaxis=y_axis_config)

# 生成图表
offline.plot({'data':data,'layout':my_layout}, filename='data/d6.html')
