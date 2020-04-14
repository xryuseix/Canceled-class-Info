from datetime import datetime
import pytz
def adddate(string):
    string += '\n( ' + datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y年%m月%d日 %H:%M:%S') + " 現在)"
    return string

date = adddate('')

print(date)