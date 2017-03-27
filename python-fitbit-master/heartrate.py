import fitbit
import gather_keys_oauth2 as Oauth2
import matplotlib.pyplot as plt
import numpy as np
 
 
"""for OAuth2.0"""
USER_ID = '228DDC'
CLIENT_SECRET = '9631c222a7d738cf657c495ec381ce37'
 
"""for obtaining Access-token and Refresh-token"""
server = Oauth2.OAuth2Server(USER_ID, CLIENT_SECRET)
server.browser_authorize()
print(server)
print('FULL RESULTS = %s' % server.oauth2.token)
print('ACCESS_TOKEN = %s' % server.oauth.token['access_token'])
 
ACCESS_TOKEN = server.oauth.token['access_token']
REFRESH_TOKEN = server.oauth.token['refresh_token']
 
"""Authorization"""
auth2_client = fitbit.Fitbit(USER_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
 
"""Getting data"""
fitbit_stats = auth2_client.intraday_time_series('activities/heart', base_date='2015-11-01', detail_level='1min')
 
"""Getting only 'heartrate' and 'time'"""
stats = fitbit_stats['activities-heart-intraday']['dataset']
 
"""Timeseries data of Heartrate"""
f1 = open('dataHR-timeseries.txt', 'w')
HR = []
for var in range(0, len(stats)):
    f1.write(stats[var]['time'])
    f1.write("\t")
    f1.write(str(stats[var]['value']))
    f1.write("\n")
    HR = HR + [stats[var]['value']]
 
f1.close()
HRmax = np.max(HR)
HRmin = np.min(HR)
plt.hist(HR, bins=len(stats), range=(HRmin,HRmax))
plt.show()