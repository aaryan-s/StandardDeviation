#import pandas as pd
#import plotly.express as px

#dataframe = pd.read_csv("projectdata.csv")

#coffee = list(dataframe["cases"])
#print("Data:",coffee)

data = [60,61,65,63,98,99,90,95,91,96]
i = 0
total=0
submean = 0.0
while i<len(data):
    total = total+data[i]
    i+=1
mean = (total/len(data))
print("Mean:",mean)


t = 0
while t<len(data):
    # running total of numerator = running total of numerator + (Data number - average)^2
    submean = float(submean) + (float(data[t])-mean)*(float(data[t])-mean)
    t+=1
print("Numerator:",submean)
fraction = submean/len(data)
print("Fraction:",fraction)
standardDeviation = pow(fraction,1/2)
print("Standard Deviation:",standardDeviation)