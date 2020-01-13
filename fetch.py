import pycrawl

url = 'http://www.ritsumei.ac.jp/academic-affairs/status/'
doc = pycrawl.PyCrawl(url)

# access another url
# doc.get('another url')

# get current url
# print(doc.url)

# get current site's html
print(doc.html)

# get <table> tags as dict
# print(doc.tables)