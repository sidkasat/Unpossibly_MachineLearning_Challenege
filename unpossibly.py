import time
import json
import requests
import matplotlib.pyplot as plt
import datetime


url="http://challenges.instagram.unpossib.ly/api/live"
API="lhbTFzIA5bOCmIKlXd9VNuRATsWl9ohv"
email="siddhantkasat@gmail.com"

r = requests.get(url, auth=(email, API))
data=r.json()
print(data)
'''for (k,v) in data.items():
    if(k=="accounts"):
        for x in v:
            for val in x.values():
                #print(type(val))
                if(type(val)==list):
                    xs=[]
                    ys=[]
                    i=0
                    for j in val:
                        i+=1
                        #day_time=datetime.datetime.fromtimestamp(int(j['date'])).strftime('%Y-%m-%d %H:%M:%S')
                        #day_time=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(j['date'])))
                        likes=j['snapshot']['likes']
                        print(j['id']," at ",day_time," : ",likes)
                        xs.append(int(j['date']))
                        #xs.append(datetime.datetime.now() + datetime.timedelta(hours=i))
                        ys.append(likes)
                    #plt.scatter(xs,ys)
                    #plt.gcf().autofmt_xdate()
                    #plt.show()'''

login_payload = {"post":"1486792033180171571","likes":20153}
authentication = (email, API)  # Anyone who sees your authorization will be able to get this anyway
url2 = 'http://challenges.instagram.unpossib.ly/api/submissions'
response = requests.post(url2, json=login_payload, auth=authentication)
print(response.json())
                    
                        
