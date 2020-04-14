import pycrawl

def fetch():
    url = 'http://www.ritsumei.ac.jp/academic-affairs/status/'
    doc = pycrawl.PyCrawl(url)

    # 休講理由をキー，キャンパス名を配列
    statuses = {}

    # キャンパス名
    campus = ['井笠', 'びわこ・くさつ', '大阪いばらき', '大阪梅田', '朱雀']

    
    for i in range(1, 6):
        status = doc.xpath('//*[@id="main"]/section[1]/section['+str(i)+']/div/div[2]/div[2]/ul/li/span[1]').inner_text()[0:-2]
        if status in statuses:
            statuses[status].append(campus[i - 1])
        else:
            statuses[status] = [campus[i - 1]]
    
    tweet = []
    
    for key in statuses.keys():
        if key != '通常通り':
            if len(statuses[key]) == 5:
                campusString = '全'
            else:
                campusString = ','.join(statuses[key])
            tweet.append("【立命館大学休講情報】\n本日" + campusString + "キャンパスは「" + key + "」です．")
    
    return tweet, statuses, campus