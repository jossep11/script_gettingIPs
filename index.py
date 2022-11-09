import requests 
import os
import json
import asyncio
from decouple import config

async def main():
    url1='https://billing.osnetpr.com/api/2.0/?method=support.ticket_list&queue=57&type=Open'
    user=config('user')
    passw=config('password')

    r=requests.get(url1, auth=(user, passw), verify=False)
    data1= r.json()
    jsonKeys = data1['data'].keys()

    for i in jsonKeys:
        service_id=data1['data'][i]['service_id']
        if service_id!='0':
            url2='https://billing.osnetpr.com/api/2.0/?method=client.service_get&service_id='+service_id+'&metadata=1'
            r2=requests.get(url2, auth=(user, passw), verify=False)    
            await asyncio.sleep(1)
            data2= r2.json()
            print(data2['data']['metadata']['ip_address'])
            print('=========================== break ====================================================================')

asyncio.run(main())

