import requests
from bs4 import BeautifulSoup
import json

def checkjquery(url,getversion,verbose):

    data = {}
    resp=requests.get(url,timeout=5)

    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')
        data['success'] = 'true'
        f=False
        for src in soup.find_all('script'):
            findjquery=str(src.get('src')).find('jquery')
            if findjquery !=-1:
                data['uses_jquery'] = 'yes'
                f=True;
                if getversion=='yes':
                    version=str(src.get('src'))[findjquery+7:].split('.')
                    data['version'] = version[0][-2:]+'.'+version[1]
                if verbose=='yes':
                    data['found_in_line'] = str(src)

        if f!=True:
        	data['uses_jquery'] = 'no'

        #json_data = json.dumps(data)
        return data

    else:
    	data['success'] = 'false'
    	#json_data = json.dumps(data)
    	return data
