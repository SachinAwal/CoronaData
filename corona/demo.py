import pandas as pd 
from matplotlib import pyplot as plt

plt.style.use("ggplot")

x = pd.read_excel("coData.xlsx")
data = pd.DataFrame(x)
xData = data.iloc[1:7,1]
yData1 = data.iloc[1:7,2]
yData2 = data.iloc[1:7,4]
yData3 = data.iloc[1:7,3]
yData4 = data.iloc[1:7,6]

fig1, (ax1) = plt.subplots()
fig2, (ax2, ax3) = plt.subplots(nrows= 2, ncols= 1, sharex= True)

ax1.plot(xData,yData1, linestyle= '--', marker= '.', label='Total Cases')
ax1.plot(xData,yData4, linestyle= 'dashed', marker= '.', label='Total Recovered')
ax1.legend()
ax1.set_title("Graph of total cases and total recovered in top 7 countries")
ax1.set_xlabel("Name of Countries")
ax1.set_ylabel("No. of  total cases and total recovered")

ax2.plot(xData,yData2, color= 'black', linestyle= 'dotted', marker= 'o', label='Total Deaths')
ax2.legend()
ax2.set_title("Graph of total death and new cases in top 7 countries")
ax2.set_ylabel("Total no. of deaths")

ax3.plot(xData,yData3, color= 'b', marker= '.', label='New Cases')
ax3.legend()
ax3.set_xlabel("Name of Countries")
ax3.set_ylabel("No. of new cases")

ax1.get_yaxis().get_major_formatter().set_scientific(False)

plt.tight_layout()

plt.show()

fig1.savefig("fig1.png")
fig2.savefig("fig2.png")