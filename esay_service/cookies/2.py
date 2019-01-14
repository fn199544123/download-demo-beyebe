import requests
from pprint import pprint
import json

for i in range(5684100,5684800):
    params='url_key=36c40a0dfff66f6cf2ee77ad43bd35f5&tokenId=gFkbRMGbozb7gLHtdjG7qA==&encryptdata={"organizationid":"%d"}'%i
    resp = requests.get('http://api.gbdex.com/trade.tollgate/gbdex10/GetFreeEnt_AllInfo', params=params)
    resp = json.loads(resp.text)
    # resp = json.dumps(resp)
    print(resp)