import requests
import configparser
import base64

config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')
cwaClientId = config['CW']['clientid']
cwaAuth = config['CW']['auth']
cwaUrlPre = 'https://api-na.myconnectwise.net/v4_6_release/apis/3.0/'
cwaApiType = 'company/companies/'
cwaApiType = 'sales/opportunities/'
cwaApiType = 'service/boards/'
# cwaOppId = '6273'
cwaApiCall = ''
cwaApiParamPre = '?'
cwaPages = [1, 2, 3, 4, 5, 6]
pageSize = 500
response = ''

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
    cwaApiUrl = cwaUrlPre + cwaApiType + cwaApiCall + cwaApiParamFinal
    print(cwaApiUrl)
    cwaOppReq = requests.get(str(cwaApiUrl), headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
    response = cwaOppReq.json()
    print(len(response))
    for respEntry in response:
        if str(respEntry['name']) == 'Service Requests':
            print(respEntry)
    # print(response)
    if len(response) != pageSize:
        break
print('done')

