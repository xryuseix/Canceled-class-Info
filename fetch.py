import pycrawl

def fetch():
    url = 'http://www.ritsumei.ac.jp/academic-affairs/status/'
    doc = pycrawl.PyCrawl(url)

    # 休講情報を持つ配列
    status = []

    # キャンパス名
    campus = ['井笠', 'びわこ・くさつ', '大阪いばらき', '大阪梅田', '朱雀']

    # 井笠キャンパス
    status.append(doc.xpath('//*[@id="main"]/section[1]/section[1]/div/div[2]/div[2]/ul/li/span[1]').inner_text()[0:-2])

    # びわこ・くさつキャンパス
    status.append(doc.xpath('//*[@id="main"]/section[1]/section[2]/div/div[2]/div[2]/ul/li/span[1]').inner_text()[0:-2])

    # 大阪いばらきキャンパス
    status.append(doc.xpath('//*[@id="main"]/section[1]/section[3]/div/div[2]/div[2]/ul/li/span[1]').inner_text()[0:-2])

    # 大阪梅田キャンパス
    status.append(doc.xpath('//*[@id="main"]/section[1]/section[4]/div/div[2]/div[2]/ul/li/span[1]').inner_text()[0:-2])

    # 朱雀キャンパス
    status.append(doc.xpath('//*[@id="main"]/section[1]/section[5]/div/div[2]/div[2]/ul/li/span[1]').inner_text()[0:-2])

    tweet = []

    for i in range(len(status)):
        if status[i] != '通常通り':
            tweet.append("【立命館大学休講情報】\n" + campus[i] + "は「" + status[i] + "」です．")

    return tweet, status, campus