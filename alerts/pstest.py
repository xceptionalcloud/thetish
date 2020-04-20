import requests
import configparser
import base64
import psycopg2
from datetime import datetime

config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')
psqlUser = config['POSTGRES']['user']
psqlPass = config['POSTGRES']['pass']
psqlDb = config['POSTGRES']['db']
cwaClientId = config['CW']['clientid']
cwaAuth = config['CW']['auth']

resource = 'alangford1'

cwaUrlPre = 'https://api-na.myconnectwise.net/v4_6_release/apis/3.0/'
cwaApiType = 'service/tickets'
# cwaTicketId = '?conditions=board/name="Alerts" and status/name="New-LM" and company/name="Juno Therapeutics, Inc."'
cwaTicketId = '?conditions=board/name="Alerts" and status/name!="Closed"'
# cwaTicketId = '/64609'
cwaApiUrl = cwaUrlPre + cwaApiType + cwaTicketId
cwaApiCall = ''
cwaApiParamPre = '&'
cwaPages = [1, 2, 3, 4, 5, 6]
pageSize = 500
response = ''

#cwaOppReq = requests.get(str(cwaApiUrl), headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
#response = cwaOppReq.json()
#print(len(response))
#print(response)

#for respEntry in response:
    #print(respEntry['summary'])
    #print(str(respEntry['id']))
counter = 0
for page in cwaPages:
    iterator = 0
    cwaApiParams = {'pageSize': str(pageSize), 'page': str(page)}
    cwaApiParamPkg = ''
    for entry, value in cwaApiParams.items():
        iterator+=1
        if iterator == len(cwaApiParams):
            cwaApiParamPkg = str(cwaApiParamPkg) + str(entry) + '=' + str(value)
        else:
            cwaApiParamPkg = str(cwaApiParamPkg) + str(entry) + '=' + str(value) + '&'
    cwaApiParamFinal = cwaApiParamPre + cwaApiParamPkg
    # cwaApiParamFinal = '?id=64418'
    cwaApiUrl = cwaUrlPre + cwaApiType + cwaTicketId + cwaApiParamFinal
    print(cwaApiUrl)
    cwaOppReq = requests.get(str(cwaApiUrl), headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
    response = cwaOppReq.json()
    print(len(response))
    for respEntry in response:
        if str(respEntry['company']['name']) == 'PriceSmart':
            print(respEntry['summary'])
            print(respEntry['status']['name'])
            counter+=1
            dateEntered = datetime.strptime(str(respEntry['_info']['dateEntered']), '%Y-%m-%dT%H:%M:%SZ')
            print(dateEntered)
    # print(response)
    if len(response) != pageSize:
        break
print('done ' + str(counter))

