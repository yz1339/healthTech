import pandas as pd
import json
import matplotlib.pyplot as plt

def showComparison(fileName1, fileName2, header, t):
	with open(fileName1, 'r') as f:
	    data_1=json.load(f)

	with open(fileName2, 'r') as f:
	    data_2=json.load(f)

	dataf1 = data_1[header]
	dataf1 = json.dumps(dataf1)

	dataf2 = data_2[header]
	dataf2 = json.dumps(dataf2)

	df1=pd.read_json(dataf1)
	df1=df1.rename(columns = {'value':'2017-03-(12-19)'})
	df1['dateTime'] = df1['dateTime'].map(lambda t: t.strftime('%Y-%m-%d'))

	df2=pd.read_json(dataf2)
	df2=df2.rename(columns = {'value':'2016-01-(17-24)'})
	df2['dateTime'] = df2['dateTime'].map(lambda t: t.strftime('%Y-%m-%d'))

	frames = [df1, df2]
	result = pd.concat(frames,axis=1)

	print(result)

	#Sleep in Minutes
	# df1.plot.bar(x='dateTime', y='value')
	result.plot.bar(title=t)

	plt.show()

def toHeartRateDF(fileName):
	with open(fileName, 'r') as f:
	    data_heart=json.load(f)
	dataf = data_heart['activities-heart']

	dataf = json.dumps(dataf)

	df=pd.read_json(dataf)
	df['value'] = df['value'].map(lambda v: v['heartRateZones'][1]['minutes'] + v['heartRateZones'][2]['minutes'] + v['heartRateZones'][3]['minutes'])
	# df=df.rename(columns = {'value':'2017-03-(12-19)'})
	df['dateTime'] = df['dateTime'].map(lambda t: t.strftime('%Y-%m-%d'))

	return df

def showHeartRateComparison():
	df1 = toHeartRateDF("datadumpHeart3.json")
	df2 = toHeartRateDF("datadumpHeart2.json")
	df1=df1.rename(columns = {'value':'2017-03-(12-19)'})
	df2=df2.rename(columns = {'value':'2016-01-(17-24)'})
	frames = [df1, df2]
	result = pd.concat(frames,axis=1)

	print(result)
	result.plot.bar(title='Minutes of heart rate >= 98')

	plt.show()

	

# showComparison('datadumpSleep3.json', 'datadumpSleep2.json', 'sleep-minutesAsleep', 'Sleep Comparison')
# showComparison('datadumpSteps3.json', 'datadumpSteps2.json', 'activities-steps', 'Steps Comparison')
# showComparison('datadumpSedentary3.json', 'datadumpSedentary2.json', 'activities-minutesSedentary', 'Sedentary Comparison')

showHeartRateComparison()




