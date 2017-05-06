#encoding:utf8
import os, sys, pdb, requests, time, json
import datetime, humanize

def getNews():
    url = ur'https://wechat.gomass.xyz/polls/getLifeFeed'

    timestamp = str(int(time.time()) * 1000)
    latitude, longitude = '40.00721', '116.3199'
    r = requests.post(url, 
            data = {'user_raw_id': 'appname',
                'app_request_timestamp':timestamp,
                'latitude':latitude,
                'longitude':longitude,},
            verify=False)
    lifenews = json.loads(r.text)
    infoList = list()
    for ind in xrange(0, len(lifenews['contentList'])):
        cellInfo = dict()
        cellInfo['nickname'] = lifenews['nicknameList'][ind]
        cellInfo['timestamp'] = lifenews['timestampList'][ind]
        cellInfo['content'] = lifenews['contentList'][ind]
        cellInfo['lifeimagehash'] = lifenews['lifeImageHashList'][ind]
        cellInfo['profileimagehash'] = lifenews['profileImageHashList'][ind]
        cellInfo['wechatprofileimage'] = lifenews['wechat_profileimageList'][ind]
        cellInfo['likecount'] = lifenews['likecountList'][ind]

        # Converted info
        cellInfo['datetime'] = toDatetime(lifenews['timestampList'][ind])
        cellInfo['humantime'] = toHumantime(lifenews['timestampList'][ind])
        cellInfo['htmlcontent'] = htmlProcess(cellInfo['content'])
        infoList.append(cellInfo)


    return infoList

def toHumantime(timestamp):
    timegap = time.time() - int(timestamp) / 1000 
    humantime = humanize.naturaltime(timegap)
    return humantime

def htmlProcess(text):
    # htmlcontent = text.replace('\n', '</p><br />\n<p>')
    paragraphList = text.split('\n')
    return paragraphList


def toDatetime(timestamp):
    '''Convert unix timestamp to datetime.
    timestamp: in ms.
    '''
    datestr = datetime.datetime.fromtimestamp(int(timestamp) / 1000).strftime('%Y-%m-%d %H:%M:%S')
    return datestr

if __name__ == '__main__':
    getNews()
    # print toDatetime('1493992297473')

