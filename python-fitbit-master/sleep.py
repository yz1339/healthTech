import fitbit
import ConfigParser
import json
 
#Load Settings
parser = ConfigParser.SafeConfigParser()

keysFile = open('results.txt', 'r')

access_token = ''
refresh_token = ''
for line in keysFile:
	if 'access_token' in line:
		access_token = line[14:]
	if 'refresh_token' in line:
		refresh_token = line[16:]


parser.read('config.ini')


CI_id              = # parser.get('Login Parameters', 'CLIENT_ID')
CI_client_secret   = # parser.get('Login Parameters', 'CLIENT_SECRET')
CI_access_token    = access_token
CI_refresh_token   = refresh_token

authd_client = fitbit.Fitbit(CI_id, CI_client_secret, oauth2=True, access_token=CI_access_token, refresh_token=CI_refresh_token)

#intradayS = authd_client.intraday_time_series('activities/steps', base_date    = '2015-06-14', detail_level = '1hour', start_time   = None, end_time     = None)
intradayS = authd_client.time_series('activities/steps', base_date    = '2017-03-12', end_date = '2017-03-19')
f = open('datadumpSteps3.json', 'w')
json.dump(intradayS, f)

intradayH = authd_client.time_series('activities/heart', base_date    = '2017-03-12', end_date = '2017-03-19')

f = open('datadumpHeart3.json', 'w')
json.dump(intradayH, f)

intradaySedentary = authd_client.time_series('activities/minutesSedentary', base_date    = '2017-03-12', end_date = '2017-03-19')

f = open('datadumpSedentary3.json', 'w')
json.dump(intradaySedentary, f)


intradaySleep = authd_client.time_series('sleep/minutesAsleep', base_date    = '2017-03-12', end_date = '2017-03-19')

f = open('datadumpSleep3.json', 'w')
json.dump(intradaySleep, f)

# intradaySleep2 = authd_client.time_series('sleep/minutesAsleep', base_date    = '2016-01-17', end_date = '2016-01-24')

# f = open('datadumpSleep2.json', 'w')
# json.dump(intradaySleep2, f)
'''
