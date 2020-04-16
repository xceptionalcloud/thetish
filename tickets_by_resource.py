import requests
import configparser
import base64
import psycopg2

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
cwaTicketId = '?conditions=resources="{resource}"'.format(resource=resource)
cwaApiUrl = cwaUrlPre + cwaApiType + cwaTicketId
cwaApiCall = ''
cwaApiParamPre = '?'
cwaPages = [1, 2, 3, 4, 5, 6]
pageSize = 500
response = ''
psqlConn = psycopg2.connect(database=psqlDb, user=psqlUser, host='localhost', password=psqlPass)
psqlConn.autocommit = True
psqlCur = psqlConn.cursor()

psqlCur.execute('SELECT * from cwatix')
cwaTix = psqlCur.fetchall()
print(cwaTix)

cwaOppReq = requests.get(str(cwaApiUrl), headers={'Authorization': str(cwaAuth), 'Accept': 'application/json', 'clientId': str(cwaClientId)})
response = cwaOppReq.json()
#print(len(response))
# print(response)
for respEntry in response:
    print(respEntry['summary'])
    print(str(respEntry['id']))
    print(cwaTix)
    print('printed shiz')
    cleanSumm = str(respEntry['summary']).replace(':', '')
    print('cleanSumm ' + str(cleanSumm))
    try:
        print('yea')
        print(respEntry['contact'])
    except:
        print('nah')
        print(respEntry['contactName'])
    if len(cwaTix) > 0 and str(respEntry['id']) in cwaTix['cwaid']:
        print('this entry is already being tracked!')
    else:
        print('got some work to do')
        psqlCur.execute("""INSERT INTO cwatix (
            cwaid,
            cwasummary,
            cwastatus,
            cwacompany,
            cwacontact,
            cwaagreement
        ) VALUES (
            {id},
            '{summary}',
            '{status}',
            '{company}',
            '{contact}',
            '{agreement}'
        )""".format(
            id=int(respEntry['id']),
            summary=cleanSumm,
            status=str(respEntry['status']['name']),
            company=str(respEntry['company']['name']),
            contact=str(respEntry['contactName']),
            agreement=str(respEntry['agreement']['name'])
        ))
# print(response)

print('done')

