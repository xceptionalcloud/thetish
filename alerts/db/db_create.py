import requests
import configparser
import base64
import psycopg2

config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')
psqlUser = config['POSTGRES']['user']
psqlPass = config['POSTGRES']['pass']
psqlDb = config['POSTGRES']['db']

psqlConn = psycopg2.connect(database=psqlDb, user=psqlUser, host='localhost', password=psqlPass)
psqlConn.autocommit = True
psqlCur = psqlConn.cursor()
psqlCur.execute("""CREATE TABLE cwatix (
    cwaid INTEGER PRIMARY KEY,
    cwasummary TEXT,
    cwastatus TEXT,
    cwacompany TEXT,
    cwacontact TEXT,
    cwaagreement TEXT
)""")

'''
cwaClientId = config['CW']['clientid']
cwaAuth = config['CW']['auth']
cwaUrlPre = 'https://api-na.myconnectwise.net/v4_6_release/apis/3.0/'
cwaApiType = 'company/companies/'
cwaApiType = 'sales/opportunities/'
cwaApiType = 'service/boards/'
cwaApiType = 'service/tickets'
cwaTicketId = '?conditions=resources="alangford1"'
cwaApiCall = ''
cwaApiParamPre = '?'
cwaPages = [1, 2, 3, 4, 5, 6]
pageSize = 500
response = ''

for page in cwaPages:
    iterator = 0
    # cwaApiParams = {'pageSize': str(pageSize), 'page': str(page)}
    # cwaApiParamPkg = ''
    # for entry, value in cwaApiParams.items():
        # iterator+=1
        # if iterator == len(cwaApiParams):
            # cwaApiParamPkg = str(cwaApiParamPkg) + str(entry) + '=' + str(value)
        # else:
            # cwaApiParamPkg = str(cwaApiParamPkg) + str(entry) + '=' + str(value) + '&'
    # cwaApiParamFinal = cwaApiParamPre + cwaApiParamPkg
    cwaApiUrl = cwaUrlPre + cwaApiType + cwaTicketId
    print(cwaApiUrl)
    cwaOppReq = requests.get(str(cwaApiUrl), headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
    response = cwaOppReq.json()
    print(len(response))
    # print(response)
    for respEntry in response:
        # if str(respEntry['name']) == 'Service Requests':
        print(respEntry['summary'])
    # print(response)
    if len(response) != pageSize:
        break
'''
print('done')

