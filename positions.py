import os
import requests
import json

from mapLight.dirs import *
from mapLight.key import apiKey



def downloadBills(jurisdiction,session,includePositions=True,allBills=False):
    params = {'jurisdiction':jurisdiction,
                'session':session,
                'include_organizations':int(includePositions),
                'has_organizations':int(not allBills),
                'apikey':apiKey}

    url = r'http://classic.maplight.org/services_open_api/map.bill_list_v1.json'
    result = requests.get(url,params)

    result.raise_for_status()

    return result.json()['bills']


if __name__ == '__main__':
    if not os.path.isdir(positionsDir):
        os.makedirs(positionsDir)

    jurisdiction = 'us'
    # Download all sessions of congress
    for session in range(109,116):
        print('downloading {} session {}'.format(jurisdiction,session))
        bills = downloadBills(jurisdiction='us',session=session)

        with open(os.path.join(positionsDir,'{}_{}.json'.format(jurisdiction,session)),'w',encoding='utf8') as f:
            json.dump(bills,f)
