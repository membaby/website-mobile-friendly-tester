import urllib.parse as parser
import urllib.request as urllib2
import concurrent.futures
import json
import time

api_Key = 'INSERT_YOUR_API_KEY'
websites = ['https://facebook.com', 'https://github.com', 'https://google.com', 'https://cit.gg']

def isMobileFriendly(webURL):
    parameters = {
    'url': webURL,
    'key': api_Key
    }

    data = bytes(parser.urlencode(parameters), encoding='utf-8')

    try:
        response = urllib2.urlopen(url='https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run', data=data)
        data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
        
        if data['testStatus']['status'] == 'COMPLETE':
            if data['mobileFriendliness'] == 'MOBILE_FRIENDLY':
                mFriendly = True
            elif data['mobileFriendliness'] == 'NOT_MOBILE_FRIENDLY':
                mFriendly = False
            else:
                mFriendly = 'Unspecified'
        else:
            mFriendly = 'Unreachable'
            print(data['testStatus']['status'])
                    
    except Exception as error:
        if '502' in str(error):
            mFriendly = True
    finally:
        print(f'{webURL} {mFriendly}')

with concurrent.futures.ThreadPoolExecutor(max_workers=15000) as executor:
    print('* Starting Session..')
    for i in websites:
        executor.submit(isMobileFriendly, i)
        time.sleep(1)
